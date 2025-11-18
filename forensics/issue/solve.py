import os
import re
import base64
import binascii

LOG_ROOT = "."   # scan folder saat ini

# regex patterns
REGEX_BASE64 = re.compile(r"[A-Za-z0-9+/]{16,}={0,2}")
REGEX_HEX    = re.compile(r"\b[0-9a-fA-F]{20,}\b")

SUSP_KEYWORDS = [
    "secret", "debug", "admin", "payload",
    "exploit", "token", "flag", "shadow"
]


def scan_log_file(filepath):
    findings = []
    try:
        with open(filepath, "r", errors="ignore") as f:
            for line in f:
                # keyword based
                if any(k in line.lower() for k in SUSP_KEYWORDS):
                    findings.append(("keyword", line.strip()))

                # base64
                b64 = REGEX_BASE64.findall(line)
                if b64:
                    findings.append(("base64", b64))

                # hex
                hx = REGEX_HEX.findall(line)
                if hx:
                    findings.append(("hex", hx))

                # long line
                if len(line) > 300:
                    findings.append(("longline", line[:200] + "..."))
    except:
        pass

    return findings


def scan_bin_file(filepath):
    data = open(filepath, "rb").read()
    print(f"[+] Scanning binary: {filepath} ({len(data)} bytes)")

    results = {}

    # look for printable ASCII → possible base64
    ascii_text = ''.join(chr(c) if 32 <= c < 127 else " " for c in data)
    b64 = REGEX_BASE64.findall(ascii_text)
    if b64:
        decoded = []
        for blob in b64:
            try:
                decoded.append(base64.b64decode(blob))
            except:
                pass
        if decoded:
            results["base64"] = decoded
            print("    [+] base64 payload detected")

    # look for magic headers
    if b"\x89PNG" in data:
        print("    [+] embedded PNG found")
        idx = data.find(b"\x89PNG")
        end = data.find(b"IEND", idx)
        if end != -1:
            results["png"] = data[idx:end+4]

    if b"\x1f\x8b" in data:  # gzip
        print("    [+] gzip header detected")

    return results


def main():
    suspicious_results = {}

    print("[*] Scanning directory for log/bin anomalies...\n")

    for root, dirs, files in os.walk(LOG_ROOT):
        for fname in files:
            path = os.path.join(root, fname)

            # Large logs = suspicious
            size = os.path.getsize(path)

            if fname.endswith(".log"):
                findings = scan_log_file(path)
                if findings:
                    suspicious_results[path] = findings

            if fname.endswith(".bin"):
                results = scan_bin_file(path)
                if results:
                    suspicious_results[path] = results

            # report oversized logs (might hide payload)
            if size > 5_000_000:  # >5MB
                print(f"[!] Large file: {fname}  ({size/1024/1024:.2f} MB)")

    print("\n========== SUSPICIOUS FILES ==========\n")
    for path, findings in suspicious_results.items():
        print(f"[+] {path}")
        for f in findings:
            print("   ", f)
        print()

    print("[*] Done.")


if __name__ == "__main__":
    main()

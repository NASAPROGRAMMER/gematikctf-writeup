import re
import urllib.parse

log = "access.log"

# Pola request method + path
request_regex = re.compile(r'\"(GET|POST|PUT|DELETE|PATCH) (.*?) HTTP')

# Pola command injection patterns
cmd_like = [
    r';', r'\|', r'&&', r'\$\(', r'`', r'cmd=', r'bash', r'sh'
]

cmd_regex = re.compile('|'.join(cmd_like), re.IGNORECASE)

# Pola flag
flag_regex = re.compile(r'gematik\{.*?\}')

with open(log, "r", encoding="utf-8", errors="ignore") as f:
    for line_num, line in enumerate(f, 1):

        req = request_regex.search(line)
        if not req:
            continue

        method, path = req.group(1), req.group(2)

        # decode URL-encoded (%xx)
        decoded_path = urllib.parse.unquote(path)

        # Fokus: request ke /upload
        if "/upload" in path or "/upload" in decoded_path:

            print(f"\n[UPLOAD DETECTED] at line {line_num}")
            print("Raw:", line.strip())
            print("Decoded path:", decoded_path)

            # cek command-like parameter
            if cmd_regex.search(decoded_path):
                print(" -> Suspicious parameter FOUND")

        # Cari flag yang disisipkan dimanapun
        flag = flag_regex.search(decoded_path)
        if flag:
            print(f"\n[FLAG FOUND] at line {line_num}")
            print(flag.group(0))

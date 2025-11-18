import os
import re

print("[*] Scanning flags0.txt sampai flags9.txt ...\n")

real_flags = []

for i in range(10):
    filename = f"flags{i}.txt"
    if not os.path.exists(filename):
        continue

    with open(filename, "r", errors="ignore") as f:
        for line in f:
            line = line.strip()

            # Cari flag dengan pola Gematik/Gemastik
            if re.search(r"Gem[aA]t?ik2025\{.*\}", line):
                
                # Skip fake flags
                if "fake_flag" in line.lower():
                    continue

                real_flags.append(line)

print("\n[*] Real flags ditemukan:")
if not real_flags:
    print("=> (Tidak ada flag asli ditemukan)")
else:
    for rf in real_flags:
        print(" -", rf)

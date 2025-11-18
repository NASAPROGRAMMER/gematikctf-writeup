data_hex = (
    "0a2e529228274bb6e344ad4cc37f96f4"
    "a45efc9b744768b10b0cdb0c4860c17a"
    "cbf74b9db2a9e43c99162bb8"
)

# Convert hex → bytes
ct = bytes.fromhex(data_hex)

# constants from binary
rcx = 0xdeadbeefcafebabe
rdi = 0x9e3779b97f4a7c15
rsi = 0x0123456789abcdef

pt = bytearray()

for b in ct:
    rax = rcx
    rax ^= (rax << 13) & 0xffffffffffffffff
    rax ^= (rax >> 7)
    rax ^= (rax << 17) & 0xffffffffffffffff
    rax ^= rdi

    rcx = (rax + rsi) & 0xffffffffffffffff

    pt.append(b ^ (rcx & 0xff))

print(pt.decode(errors="ignore"))

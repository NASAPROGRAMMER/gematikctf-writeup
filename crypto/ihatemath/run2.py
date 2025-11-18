from ellipticcurve import EllipticCurve, Point
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode

# Curve parameters
p = 316474165760433275517489571416399628297
curve = EllipticCurve(13, 245, p)

# Given point
Px = 15357222892792096609
Py = 158037364221316467013381180746196242613
P = Point(curve, Px, Py)

# Cipher data from challenge
ciphertext = b64decode("qLsr8ecqPrhNmWkYsOQSgUbk5FxnKLb0tGAyLuMdyOpitWlrh3quficDkCrFGoNRKQjYAft+4VmeibD7Dx2V/UFV/QsYWED059TAOoBBPxoP16Tn/o3Xnh9//9gOmf3Ymevo5mbJCXVxnWGl4vT5bg==")
iv = b64decode("lt15/rRg9/dzeME1rHE4iA==")

# Compute Q = 1337 * P
k = 1337
Q = P * k
print("Q =", Q)

# Derive AES key
sha1 = hashlib.sha1()
sha1.update(str(Q.x).encode())
key = sha1.digest()[:16]

# AES decrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

print("FLAG =", plaintext.decode())

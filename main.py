from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import binascii
from cryptography.hazmat.primitives.padding import PKCS7
#Refrence
#https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
import os
print("-----------------C1------------------------")
key1 = b'12345678'
#key = os.urandom(24)
nonce1 = b'12345678'#os.urandom(8)
print("KEY is")
print(key1)
print("nonce is")
print(nonce1)
cipher1 = Cipher(algorithms.TripleDES(key1), modes.OFB(nonce1))
encryptor1 = cipher1.encryptor()
c1 = encryptor1.update(b"Crypto is fun and entertaining") + encryptor1.finalize()
print("ciphertext c1 is")
print(c1)

print("-----------------C2------------------------")
key2 = b'12345678abcdefghabcdefgh'
#key = os.urandom(24)
nonce2 = b'12345678'#os.urandom(8)
print("KEY is")
print(key2)
print("nonce is")
print(nonce2)
cipher2 = Cipher(algorithms.TripleDES(key2), modes.OFB(nonce2))
encryptor2 = cipher2.encryptor()
c2 = encryptor2.update(b"Crypto is fun and entertaining") + encryptor2.finalize()
print("ciphertext c2 is")
print(c2)

print("-----------------C3------------------------")
key3 = b'abcdefghabcdefgh12345678'
#key = os.urandom(24)
nonce3 = b'12345678'#os.urandom(8)
print("KEY is")
print(key3)
print("nonce is")
print(nonce3)
cipher3 = Cipher(algorithms.TripleDES(key3), modes.OFB(nonce3))
encryptor3 = cipher3.encryptor()
c3 = encryptor3.update(b"Crypto is fun and entertaining") + encryptor3.finalize()
print("ciphertext c3 is")
print(c3)
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 2048 bit RSA key pair generate करतो
key        = RSA.generate(2048)
public_key = key.publickey()

# Message
message = b'HelloRSA'

# Encrypt (Public key वापरून)
cipher_enc = PKCS1_OAEP.new(public_key)
encrypted  = cipher_enc.encrypt(message)

# Decrypt (Private key वापरून)
cipher_dec = PKCS1_OAEP.new(key)
decrypted  = cipher_dec.decrypt(encrypted)

# Output
print("Original Message :", message.decode())
print("Key size         :", key.size_in_bits(), "bits")
print("Public key (e)   :", public_key.e)
print("Encrypted (hex)  :", encrypted.hex()[:60], "...")
print("Encrypted length :", len(encrypted), "bytes")
print("Decrypted Text   :", decrypted.decode())

# Step 1 - Library install करा:
# pip install pycryptodome
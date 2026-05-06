from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Key आणि plaintext
key       = b'0123456789abcdef'   # exactly 16 bytes
plaintext = b'HelloAESWorld!!!'   # exactly 16 bytes

# Encrypt
cipher_enc    = AES.new(key, AES.MODE_ECB)
padded_text   = pad(plaintext, 16)
encrypted     = cipher_enc.encrypt(padded_text)

# Decrypt
cipher_dec       = AES.new(key, AES.MODE_ECB)
decrypted_padded = cipher_dec.decrypt(encrypted)
decrypted        = unpad(decrypted_padded, 16)

# Output
print("Key              :", key)
print("Original Text    :", plaintext.decode())
print("Padded Text      :", padded_text)
print("Encrypted (hex)  :", encrypted.hex())
print("Encrypted (bytes):", encrypted)
print("Decrypted Text   :", decrypted.decode())

# Step 1 - Library install करा:
# pip install pycryptodome
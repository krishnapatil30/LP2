from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Key आणि plaintext
key       = b'DESKEY01'    # exactly 8 bytes
plaintext = b'HelloDES'    # exactly 8 bytes

# Encrypt
cipher_enc    = DES.new(key, DES.MODE_ECB)
padded_text   = pad(plaintext, 8)
encrypted     = cipher_enc.encrypt(padded_text)

# Decrypt
cipher_dec       = DES.new(key, DES.MODE_ECB)
decrypted_padded = cipher_dec.decrypt(encrypted)
decrypted        = unpad(decrypted_padded, 8)

# Output
print("Key              :", key)
print("Original Text    :", plaintext.decode())
print("Padded Text      :", padded_text)
print("Encrypted (hex)  :", encrypted.hex())
print("Encrypted (bytes):", encrypted)
print("Decrypted Text   :", decrypted.decode())

# Step 1 - Library install करा:
# pip install pycryptodome
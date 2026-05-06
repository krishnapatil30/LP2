import math

def encrypt(message, key):
    cipher = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            cipher[col] += message[pointer]
            pointer += key          # पुढचा column skip करतो

    return ''.join(cipher)


def decrypt(cipher_text, key):
    num_cols = key
    num_rows = math.ceil(len(cipher_text) / key)
    num_shaded = (num_cols * num_rows) - len(cipher_text)

    plain = [''] * num_rows
    col = 0
    row = 0

    for symbol in cipher_text:
        plain[row] += symbol
        row += 1

        if (row == num_rows) or \
           (row == num_rows - 1 and col >= num_cols - num_shaded):
            row = 0
            col += 1

    return ''.join(plain)


# Run
message   = "HELLOWORLD"
key       = 3

encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print("Original Message :", message)
print("Key (columns)    :", key)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
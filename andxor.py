s = "Hello World"
print("Original String :", s)

# AND 127 operation
and_result = ''.join(chr(ord(c) & 127) for c in s)

# XOR 127 operation (Encryption)
xor_result = ''.join(chr(ord(c) ^ 127) for c in s)

print("After AND 127   :", and_result)
print("After XOR 127   :", xor_result)

# XOR पुन्हा = Decryption
restored = ''.join(chr(ord(c) ^ 127) for c in xor_result)
print("XOR Decrypted   :", restored)

# Detail Table
print("\nChar  ASCII  AND 127  XOR 127  AND chr  XOR chr")
print("-" * 54)

for c in s:
    ascii_val = ord(c)
    and_val   = ascii_val & 127
    xor_val   = ascii_val ^ 127
    print(f"{repr(c):<7}{ascii_val:<9}{and_val:<11}{xor_val:<11}{repr(chr(and_val)):<9}{repr(chr(xor_val))}")
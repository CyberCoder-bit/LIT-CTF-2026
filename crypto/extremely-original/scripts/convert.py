alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
ciphertext="oyO+UrMXccyqeo2W+WA5jZPVXNSAyYVwGt"
known_plaintext = "LITCTF"
converted_ciphertext=[]
converted_plaintext=[]
for c in ciphertext:
    converted_ciphertext.append(alphabet.index(c))

print("Converted Ciphertext:",converted_ciphertext)
for c in known_plaintext:
    converted_plaintext.append(alphabet.index(c))

print("Converted Known-Plaintext:",converted_plaintext)

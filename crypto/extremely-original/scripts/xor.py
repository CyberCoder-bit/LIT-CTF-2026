converted_ciphertext=[40, 50, 14, 62, 20, 43, 12, 23, 28, 28, 50, 42, 30, 40, 54, 22, 62, 22, 0, 57, 35, 25, 15, 21, 23, 13, 18, 0, 50, 24, 21, 48, 6, 45]
converted_plaintext=[11, 8, 19, 2, 19, 5]
key=[]
for i in range(len(converted_plaintext)):
    key.append(converted_ciphertext[i]^converted_plaintext[i])

print("Known Key:",key)

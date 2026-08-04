key=[35, 58, 29, 60, 7, 46]
converted_ciphertext=[40, 50, 14, 62, 20, 43, 12, 23, 28, 28, 50, 42, 30, 40, 54, 22, 62, 22, 0, 57, 35, 25, 15, 21, 23, 13, 18, 0, 50, 24, 21, 48, 6, 45]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
m=64
a=21
c=27
while(len(key)<len(converted_ciphertext)):
    key.append((key[-1]*a+c)%64)

print("Full Key:", key)

recovered_values=[]

for i in range(len(key)):
    recovered_values.append(converted_ciphertext[i]^key[i])

print("Recovered Values:", recovered_values)

plaintext = ""
for i in range(len(recovered_values)):
    plaintext += alphabet[recovered_values[i]]

print(plaintext)

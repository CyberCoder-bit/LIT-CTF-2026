def convert_to_indices(string):
    converted=[]
    for char in string:
        converted.append(base64_alphabet.index(char))
    return converted

def xor(a, b):
    output=[]
    for i in range(min(len(a), len(b))):
        output.append(a[i]^b[i])
    return output

def brute_force_LCG(m):
    for possible_a in range(m):
        for possible_c in range(m):
            valid=True
            for i in range(len(key)-1):
                if (key[i+1]!=(possible_a*key[i]+possible_c)%m):
                    valid=False
            if valid:
                return possible_a, possible_c
    return 0, 0

def recover_key(known_key, key_length, m, a, c):
    while(len(known_key)<key_length):
        known_key.append((key[-1]*a+c)%m)
    return known_key

def convert_from_indices(values):
    plaintext=""
    for index in values:
        plaintext+=base64_alphabet[index]
    return plaintext

base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
ciphertext="oyO+UrMXccyqeo2W+WA5jZPVXNSAyYVwGt"
known_plaintext = "LITCTF"

# Convert ciphertext and known plaintext to indices based on base64 alphabet
converted_ciphertext = convert_to_indices(ciphertext)
converted_plaintext = convert_to_indices(known_plaintext)

print("Converted Ciphertext:", converted_ciphertext)
print("Converted Known-Plaintext:", converted_plaintext, "\n")

# XOR ciphertext with known plaintext to recover start of key
key = xor(converted_ciphertext, converted_plaintext)

print("Known Key:", key, "\n")

# Brute force LCG params
m=64
a, c = brute_force_LCG(m)

print("LCG Parameters: a = "+str(a)+", c = "+str(c)+", m = "+str(m)+"\n")

# Recover the rest of the key
key = recover_key(key, len(ciphertext), m, a, c)

print("Full Key:", key, "\n")

# Decrypt to base64 Indices
indices=xor(converted_ciphertext, key)

print("Recovered Indices:", indices, "\n")

# Convert back to base64 Characters
plaintext = convert_from_indices(indices)

print("Plaintext:", plaintext)
print("Flag", plaintext[:6]+"{"+plaintext[6:]+"}")

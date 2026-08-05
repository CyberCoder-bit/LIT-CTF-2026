# LIT CTF 2026 - Extremely Original Write-Up - Cryptography

> Author: joshadoodle

**Challenge Description:**

It seems that I have accidentally leaked my flag: oyO+UrMXccyqeo2W+WA5jZPVXNSAyYVwGt

Good thing that my computer generated keys to encrypt my flag before releasing it to the public. The flag for this challenge will be "LITCTF" followed by a string of characters. Make sure to insert curly braces yourself: "LITCTF{...}".

## Solution

**Step 1: Looking For Clues**

First, we can see that the challenge name is eXtremely ORiginal, which hides the word XOR in it, so the encryption is most likely XOR. I tried to use a repeating key by using the known LITCTF prefix, but it failed.

Looking closer at the challenge description, we can notice it says "generated", so it probably used a common algorithm like Linear Congruential Generator (LCG).

Next, we can notice that all the characters are from the base64 alphabet. So we can convert the known plaintext to numbers based on their index in the base64 alphabet, which is ```ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/```.

**Step 2: Convert to Base64**

I wrote [convert.py](scripts/convert.py) to convert them.

Output:
```bash
python3 convert.py
Converted Ciphertext: [40, 50, 14, 62, 20, 43, 12, 23, 28, 28, 50, 42, 30, 40, 54, 22, 62, 22, 0, 57, 35, 25, 15, 21, 23, 13, 18, 0, 50, 24, 21, 48, 6, 45]
Converted Known-Plaintext: [11, 8, 19, 2, 19, 5]
```

**Step 3: XOR**

After getting the ciphertext and the known plaintext, we use a common algorithm to reverse the XOR operation.

```
plaintext ^ key = ciphertext
plaintext ^ key ^ plaintext = ciphertext ^ plaintext = key
```

Thus, by xoring the plaintext and ciphertext using a tool like [XOR Calculator](https://xor.pw/#), we can get the start of the key, which is an LCG sequence.

| Plaintext | Ciphertext | Key |
|---|---|---|
| 40 | 11 | 35 |
| 50 | 8 | 58 |
| 14 | 19 | 29 |
| 62 | 2 | 60 |
| 20 | 19 | 7 |
| 43 | 5 | 46 |

I also wrote [xor.py](scripts/xor.py) to do this calculation.

Output:
```bash
python3 xor.py
Known Key: [35, 58, 29, 60, 7, 46]
```

**Step 4: Reversing LCG**

Now that we have the first part of the key, we need to reverse the LCG and calculate the rest of it.

LCG Formula: $$X_{n+1} = (a X_n + c) \pmod{m}$$

Essentially, it means you multiply the last number by a certain amount, add a certain amount, and then mod it to get the answer.

We can mathematically derive the answer, but since the modulus is 64 because we are going to map it back to base64 characters, and a and c are less than 64, then we only need to brute-force 64^2 possibilities, which is only 4096.

To brute-force, we just need to check if each pair of a and c is valid such that they generate the key values we already know. For example, $(35 a + c) \bmod 64 = 58$, $(58 a + c) \bmod 64 = 29$, etc.

I wrote [brute.py](scripts/brute.py) to find the LCG parameters.

Output:
```bash
python3 brute.py
LCG Parameters: a = 21, c = 27, m = 64
```

**Step 5: Recover Key and Decrypt**

After this, we can use the LCG params we recovered to get the rest of the key and then use this key to recover the flag by XORing it and converting it back to characters.

To recover the LCG, we continue to calculate the key based on the previous values using the formula. We do $(46 \times 21 + 27) \bmod 64 = 33$, then $(33 \times 21 + 27) \bmod 64 = 16$, etc.

After this, we just XOR the key with the ciphertext and map it back to base64 such that 1 -> A, 2 -> B, etc.

I wrote [recover.py](scripts/recover.py) to recover the flag.

Output:
```bash
python3 recover.py
Full Key: [35, 58, 29, 60, 7, 46, 33, 16, 43, 34, 37, 36, 15, 22, 41, 56, 51, 10, 45, 12, 23, 62, 49, 32, 59, 50, 53, 52, 31, 38, 57, 8, 3, 26]
Recovered Values: [11, 8, 19, 2, 19, 5, 45, 7, 55, 62, 23, 14, 17, 62, 31, 46, 13, 28, 45, 53, 52, 39, 62, 53, 44, 63, 39, 52, 45, 62, 44, 56, 5, 55]
LITCTFtH3+XOR+fuNct10n+1s/n0t+s4F3
```

After adding the curly braces, the final flag is: **LITCTF{tH3+XOR+fuNct10n+1s/n0t+s4F3}**

## Summary:

I have combined all the steps into [solve.py](solve.py).

In conclusion, here is a summary of the steps:
1. Convert everything to indices based on the base64 alphabet.
2. XOR it with the known plaintext to get the start of the key.
3. Use the start of the key to get LCG parameters.
4. Use LCG parameters to get the rest of the key.
5. Use the key to decode the ciphertext.
6. Convert from indices back to base64 alphabet.
7. Add curly braces and get **LITCTF{tH3+XOR+fuNct10n+1s/n0t+s4F3}**.

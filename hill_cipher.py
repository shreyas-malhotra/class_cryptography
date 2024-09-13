import numpy as np

alphabets = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h':7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15,
'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,'y': 24, 'z': 25}
numbers = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16:
'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24:'y', 25: 'z'}

def mod26(num):
    return num % 26

def create_key(key, key_length):
    key_matrix = np.zeros((key_length, key_length), dtype=int)
    k = 0
    for i in range(key_length):
        for j in range(key_length):
            key_matrix[i][j] = alphabets[key[k]]
            k += 1
    return key_matrix

def encrypt(plaintext, key):
    ciphertext = ''
    plaintext = ''.join(filter(str.isalpha, plaintext)).lower()

    key_length = int(len(key) ** 0.5)
    key_matrix = create_key(key, key_length)

    while len(plaintext) % key_length != 0:
        plaintext += 'x'

    plaintext_matrix = [alphabets[char] for char in plaintext]

    for i in range(0, len(plaintext_matrix), key_length):
        block = plaintext_matrix[i:i + key_length]
        block_matrix = np.array(block).reshape(key_length, 1)
        encrypted_block = np.dot(key_matrix, block_matrix)
        encrypted_block = [mod26(num) for num in encrypted_block.flatten()]
        ciphertext += ''.join(numbers[num] for num in encrypted_block)

    return ciphertext
plaintext = input("Enter your message: ")
key = 'hill'
ciphertext = encrypt(plaintext, key)
print(f"Encrypted Text: {ciphertext}")
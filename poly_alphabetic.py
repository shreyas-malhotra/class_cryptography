alphabets = 'abcdefghijklmnopqrstuvwxyz'

def generatekey(plaintext, key):
    new_key = ''
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            new_key += key[i % len(key)]
        else:
            new_key += plaintext[i]
    return new_key

def encrypt(plaintext, key):
    new_key = generatekey(plaintext, key)
    ciphertext = ''
    for i in range(len(plaintext)):
        letter = plaintext[i]
        if letter.isalpha():
            letter_lower = letter.lower()
            letter_index = alphabets.index(letter_lower)
            key_index = alphabets.index(new_key[i].lower())
            encrypted_index = (letter_index + key_index) % 26
            cipher_letter = alphabets[encrypted_index]
            if letter.isupper():
                cipher_letter = cipher_letter.upper()
            ciphertext += cipher_letter
        else:
            ciphertext += letter
    return ciphertext

def decrypt(ciphertext, key):
    new_key = generatekey(ciphertext, key)
    plaintext = ''
    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        if letter.isalpha():
            letter_lower = letter.lower()
            letter_index = alphabets.index(letter_lower)
            key_index = alphabets.index(new_key[i].lower())
            decrypted_index = (letter_index - key_index) % 26
            plain_letter = alphabets[decrypted_index]
            if letter.isupper():
                plain_letter = plain_letter.upper()
            plaintext += plain_letter
        else:
            plaintext += letter
    return plaintext

choice = input("Would you like to encrypt or decrypt a message? (e/d): ").lower()
if choice not in ['e', 'd']:
    print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
else:
    if choice == 'e':
        plaintext = input("Enter text to encrypt: ")
        key = input("Enter the key: ")
        result = encrypt(plaintext, key)
        print("Encrypted message:", result)
    elif choice == 'd':
        ciphertext = input("Enter message to decrypt: ")
        key = input("Enter the key: ")
        result = decrypt(ciphertext, key)
        print("Decrypted message:", result)
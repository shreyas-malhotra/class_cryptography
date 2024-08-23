alphabets = "abcdefghijklmnopqrstuvwxyz"
key = "zyxwvutsrqponmlkjihgfedcba"

def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        letter_lower = letter.lower()
        if letter_lower not in alphabets:
            ciphertext += letter
        else:
            index = alphabets.find(letter_lower)
            cipher_letter = key[index]
            ciphertext += cipher_letter
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        letter_lower = letter.lower()
        if letter_lower not in key:
            plaintext += letter
        else:
            index = key.find(letter_lower)
            plain_letter = alphabets[index]
            plaintext += plain_letter
    return plaintext

choice = input("Would you like to encrypt or decrypt a message? (e/d): ").lower()
if choice not in ['e', 'd']:
    print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
else:
    if choice == 'e':
        plaintext = input("Enter text to encrypt: ")
        result = encrypt(plaintext, key)
        print("Encrypted message:", result)
    elif choice == 'd':
        ciphertext = input("Enter message to decrypt: ")
        result = decrypt(ciphertext, key)
        print("Decrypted message:", result)
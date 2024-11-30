import string

all_letters = string.ascii_letters

key = 4

def encrypt(text, shift):
    cipher_txt = []
    for char in text:
        if char in all_letters:
            new_char = all_letters[(all_letters.index(char) + shift) % len(all_letters)]
            cipher_txt.append(new_char)
        else:
            cipher_txt.append(char)
    return ''.join(cipher_txt)

def decrypt(text, shift):
    decrypt_txt = []
    for char in text:
        if char in all_letters:
            new_char = all_letters[(all_letters.index(char) - shift) % len(all_letters)]
            decrypt_txt.append(new_char)
        else:
            decrypt_txt.append(char)
    return ''.join(decrypt_txt)

plain_txt = "I am studying Data Encryption"

cipher_txt = encrypt(plain_txt, key)
print("Cipher Text is:", cipher_txt)

recovered_txt = decrypt(cipher_txt, key)
print("Recovered plain text:", recovered_txt)
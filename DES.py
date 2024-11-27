from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_CBC)
    padded_text = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return binascii.hexlify(cipher.iv).decode(), binascii.hexlify(ciphertext).decode()

def des_decrypt(ciphertext_hex, iv_hex, key):
    cipher = DES.new(key, DES.MODE_CBC, iv=binascii.unhexlify(iv_hex))
    decrypted_padded_text = cipher.decrypt(binascii.unhexlify(ciphertext_hex))
    decrypted_text = unpad(decrypted_padded_text, DES.block_size).decode()
    return decrypted_text

if __name__ == "__main__":
    key = b'shreyasm'
    plaintext = 'CRYPTOGRAPHY'
    iv_hex, ciphertext_hex = des_encrypt(plaintext, key)
    decrypted_text = des_decrypt(ciphertext_hex, iv_hex, key)
    print("Encrypted Text:", ciphertext_hex)
    print("Decrypted Text:", decrypted_text)
    print("Initialization Vector:", iv_hex)
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import binascii

def encrypt(plaintext,key):
    cipher=AES.new(key, AES.MODE_CBC)
    iv=cipher.iv
    padded_plaintext=pad(plaintext.encode('utf-8'),AES.block_size)
    ciphertext=cipher.encrypt(padded_plaintext)
    return binascii.hexlify(iv).decode(), base64.b64encode(iv+ciphertext).decode('utf-8')

def decrypt(ciphertext,key):
    data=base64.b64decode(ciphertext)
    iv=data[:16]
    actual_ciphertext=data[16:]
    cipher=AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext=cipher.decrypt(actual_ciphertext)
    plaintext=unpad(padded_plaintext, AES.block_size)
    return plaintext.decode('utf-8')

if __name__ == '__main__':
    key = b'shreyasmalhotram'
    plaintext = "HELLO FRIEND"
    iv, encrypted = encrypt(plaintext, key)
    decrypted = decrypt(encrypted, key)
    print("Encrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)
    print("Initialization Vector:", iv)
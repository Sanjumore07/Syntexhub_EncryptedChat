from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import base64

# Pre-shared key (must be 16, 24, or 32 bytes)
KEY = b'mysecretpassword'  # In practice, use a secure key derivation

def encrypt_message(plaintext):
    iv = os.urandom(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(iv).decode(), base64.b64encode(ciphertext).decode()

def decrypt_message(iv_b64, ciphertext_b64):
    iv = base64.b64decode(iv_b64)
    ciphertext = base64.b64decode(ciphertext_b64)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()
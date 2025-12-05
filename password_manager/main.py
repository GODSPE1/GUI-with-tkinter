from cryptography.fernet import Fernet
import os
import json

def generate_key():
    """Generates and sava key for encryption"""
    key = Fernet.generate_key();
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

def  load_key():
    """Loads the key from the current directory named `secret.key`"""
    return open('secret.key', 'rb').read()

def encrypt_password(password: str) -> bytes:
    '''Encrypt a password'''
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password


def decrypt_password(encrypted_password):
    """Decrypts a password"""
    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password


def main():
    generate_key()
    encrypted = encrypt_password('mypassword123')
    print(f"encrypted: {encrypted}")

    decrypt = decrypt_password(encrypted)
    print(f"decryted: {decrypt}")


if __name__ == "__main__":
    main()

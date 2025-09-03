from cryptography.fernet import Fernet

# Generate a key (temporary for now)
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_message(message: str) -> bytes:
    return cipher.encrypt(message.encode())

def decrypt_message(token: bytes) -> str:
    return cipher.decrypt(token).decode()

if __name__ == "__main__":
    sample = "Hello, Cesar!"
    encrypted = encrypt_message(sample)
    print("Encrypted:", encrypted)

    decrypted = decrypt_message(encrypted)
    print("Decrypted:", decrypted)
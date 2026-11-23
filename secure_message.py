import hashlib
from cryptography.fernet import Fernet

def main():
    message = input("Enter a message: ").encode('utf-8')
    orig_hash = hashlib.sha256(message). hexdigest()

    key = Fernet.generate_key()
    cipher = Fernet(key)
    enc_msg = cipher.encrypt(message)

    rec_msg = cipher.decrypt(enc_msg)
    rec_hash = hashlib.sha256(rec_msg).hexdigest()

    print("\nOriginal sha-256:", orig_hash)
    print("Encrypted message:", enc_msg.decode("ascii"))
    print("Decrypted message:", rec_msg.decode("utf-8"))
    print("Decrypted sha-256:", rec_hash)

    if orig_hash == rec_hash:
        print("Integrity check passed")
    else:
        print("Integrity checked failed")

if __name__ == "__main__":
    main()

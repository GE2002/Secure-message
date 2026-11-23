#Secure Message
I made a python that takes a messgae, hashes it with SHA-256,
encrypts it, and then decrypts it to see if I get the same messageback.

##How to run it
1. Install the library with 'python3 -m pip install cryptography'.
2. Run 'python3 secure_message.py' and type a message.

##How it works
- **Confidentiality** - Fernet encrypts my message so someone needs the secret key to read it.
- **Integrity** - The program compares the SHA-256 hash of my original message with the hash of decrypted message. If they match, it says 'Integrity check passed'.
- **Availability** - I can recover my message while the program is running. To get it back later, I'd need to save the encrypted message and keep the key somewhere safe.
- **Entropy and key generation** - The program uses secure randomness to make a new key each time I run it. That unpredictability makes the key hard to guess. 

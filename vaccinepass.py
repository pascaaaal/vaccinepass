import hashlib
import time

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def generate_keys():
    modulus_length = 1024

    key = RSA.generate(modulus_length)
    pub_key = key.publickey()

    return key, pub_key


def encrypt_private_key(a_message, private_key):
    encryptor = PKCS1_OAEP.new(private_key)
    encrypted_msg = encryptor.encrypt(a_message)
    return encrypted_msg


def decrypt_public_key(encrypted_msg, public_key):
    encryptor = PKCS1_OAEP.new(public_key)
    decoded_decrypted_msg = encryptor.decrypt(encrypted_msg)
    return decoded_decrypted_msg


# -----------Serverside--------------
# Generating keys (shoud be serverside)
# The server create's a private key for himself (encrypting) and a public key for everyone (decrypting)
(server_pub, server_priv) = generate_keys()


# --------------Client----------------
# These data is saved on the clients devices
vaccdaten = {
    "datum": "18.05.2021",
    "name": "Pascal Faude",
    "vaccine": "BioNTech",
    "timestamp": time.time()
}
# Hashing the data to be anonymous. This is send to the sever to be encypted
hash = hashlib.sha224(str(vaccdaten).encode("utf-8"))


# -----------Doctor/Server--------------
# Encrypting the hash (it's like signing) by the server and send back
# The encrypted hash is saved on the clients device
chiper = encrypt_private_key(hash.digest(), server_priv)


# ------Client that checks Vaccine State---------
# Decrypt the hash with the public key by the server. This is done by another device
ergebnis = decrypt_public_key(chiper, server_pub)

# Check if the decrypted hash equals the hash generated with the original data on anothers phone
if ergebnis == hash.digest():
    print("Verifyed")
else:
    print("Wrong")

import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


SALT_FILE = "salt.bin"


def get_salt():
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, "rb") as file:
            return file.read()

    salt = os.urandom(16)

    with open(SALT_FILE, "wb") as file:
        file.write(salt)

    return salt


def get_key(master_password):
    salt = get_salt()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )

    key = base64.urlsafe_b64encode(
        kdf.derive(master_password.encode())
    )

    return key


def encrypt_data(data, master_password):
    key = get_key(master_password)
    fernet = Fernet(key)

    encrypted_data = fernet.encrypt(data.encode())

    return encrypted_data


def decrypt_data(encrypted_data, master_password):
    key = get_key(master_password)
    fernet = Fernet(key)

    decrypted_data = fernet.decrypt(encrypted_data)

    return decrypted_data.decode()
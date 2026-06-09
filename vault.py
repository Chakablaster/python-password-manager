import json
import os

from crypto_utils import encrypt_data, decrypt_data

VAULT_FILE = "vault.enc"


def load_vault(master_password):
    if not os.path.exists(VAULT_FILE):
        return []

    with open(VAULT_FILE, "rb") as file:
        encrypted_data = file.read()

    if not encrypted_data:
        return []

    decrypted_data = decrypt_data(encrypted_data, master_password)
    return json.loads(decrypted_data)


def save_vault(data, master_password):
    json_data = json.dumps(data, indent=4)
    encrypted_data = encrypt_data(json_data, master_password)

    with open(VAULT_FILE, "wb") as file:
        file.write(encrypted_data)


def add_entry(site, username, password, master_password):
    vault = load_vault(master_password)

    entry = {
        "site": site,
        "username": username,
        "password": password
    }

    vault.append(entry)
    save_vault(vault, master_password)


def get_entries(master_password):
    return load_vault(master_password)


def search_entries(search_term, master_password):
    vault = load_vault(master_password)
    results = []

    for entry in vault:
        if search_term.lower() in entry["site"].lower():
            results.append(entry)

    return results


def delete_entry(index, master_password):
    vault = load_vault(master_password)

    if index < 0 or index >= len(vault):
        return False

    vault.pop(index)
    save_vault(vault, master_password)
    return True
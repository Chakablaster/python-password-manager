import json
import os

VAULT_FILE = "vault.json"


def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []

    with open(VAULT_FILE, "r") as file:
        return json.load(file)


def save_vault(data):
    with open(VAULT_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_entry(site, username, password):
    vault = load_vault()

    entry = {
        "site": site,
        "username": username,
        "password": password
    }

    vault.append(entry)
    save_vault(vault)
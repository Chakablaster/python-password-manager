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

def get_entries():
    return load_vault()

def search_entries(search_term):
    vault = load_vault()
    results = []

    for entry in vault:
        if search_term.lower() in entry["site"].lower():
            results.append(entry)

    return results

def delete_entry(index):
    vault = load_vault()

    if index < 0 or index >= len(vault):
        return False

    vault.pop(index)
    save_vault(vault)
    return True
# Python Password Manager

A secure local password manager built with Python.  
It stores saved credentials in an encrypted vault file and uses a master password to unlock them.

## Features

- Add saved passwords
- View saved accounts with hidden passwords
- Search saved passwords
- Generate strong random passwords
- Delete saved passwords
- Copy passwords to clipboard
- Encrypted local vault storage
- Master password protection

## Tech Used

- Python
- cryptography
- pyperclip
- rich

## Security Notes

This app stores password data locally in an encrypted file called `vault.enc`.

Sensitive files such as `vault.enc`, `salt.bin`, `.env`, and database files are ignored using `.gitignore` and should not be uploaded to GitHub.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
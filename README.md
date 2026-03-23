# 🛡️ Secure-Vault-Generator

A lightweight, cryptographically secure password generator built with Python. 
Stop using "123456" or your cat's name – generate something that actually keeps your data safe!

## ✨ Features
- **Top-Tier Security:** Uses Python's `secrets` module (cryptographically strong) instead of the standard `random` module.
- **Customizable:** You decide the password length.
- **Toggle Options:** Choose whether to include numbers or special characters.
- **Export Function:** Option to save your generated password directly to a local `passwort.txt` file.
- **Error Handling:** Robust input validation to prevent crashes.

## 🚀 Getting Started

### Prerequisites
Make sure you have [Python 3.x](https://www.python.org/downloads/) installed on your machine.

### Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/darismmj/Secure-Vault-Generator.git](https://github.com/darismmj/pygenerator.py)

 ##  🛠️ Built With
Python 3 - The core logic.

Secrets Module - For generating secure random numbers.

String Module - For easy access to character sets (ASCII, digits, punctuation).

 ## 🔒 Security Note
This tool uses the secrets module, which is designed for cryptography and security-sensitive tasks. It provides a higher level of randomness than the standard random module, making it much harder for attackers to predict generated passwords.

 ## 🗺️Roadmap / Future Ideas
[ ] Add a Graphical User Interface (GUI) using Tkinter.

[ ] Add a "Copy to Clipboard" feature.

[ ] Create a batch mode (generate 10 passwords at once).

## 📄 License
Distributed under the MIT License. See LICENSE for more information.

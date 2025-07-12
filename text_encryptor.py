"""Utilities for encrypting and decrypting text using a repeating key."""

ALPHABET_SIZE = 26


def _shift_char(char: str, shift: int) -> str:
    """Return ``char`` shifted by ``shift`` places in the alphabet."""

    base = ord('A') if char.isupper() else ord('a')
    return chr((ord(char) - base + shift) % ALPHABET_SIZE + base)


def encrypt_text(plaintext: str, key: str) -> str:
    """Encrypt ``plaintext`` using ``key`` and return the resulting text."""

    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.lower()) - ord('a')
            encrypted_char = _shift_char(char, key_shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def encrypt_text_file(file_name: str, key: str, output_file: str) -> bool:
    """Encrypt ``file_name`` using ``key`` and save the result to ``output_file``.

    Returns ``True`` on success and ``False`` if ``file_name`` cannot be opened.
    """

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            plaintext = file.read()
    except FileNotFoundError:
        print("File not found.")
        return False

    encrypted_text = encrypt_text(plaintext, key)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(encrypted_text)
    return True

def decrypt_text_file(file_name: str, key: str, output_file: str) -> bool:
    """Decrypt ``file_name`` using ``key`` and save the result to ``output_file``."""

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            ciphertext = file.read()
    except FileNotFoundError:
        print("File not found.")
        return False

    decrypted_text = decrypt_text(ciphertext, key)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(decrypted_text)
    return True

def decrypt_text(ciphertext: str, key: str) -> str:
    """Return ``ciphertext`` decrypted with ``key``."""

    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.lower()) - ord('a')
            decrypted_char = _shift_char(char, -key_shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

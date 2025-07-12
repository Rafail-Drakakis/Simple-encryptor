import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import text_encryptor


def test_encrypt_decrypt_text_roundtrip():
    message = "Hello World!"
    key = "abc"
    encrypted = text_encryptor.encrypt_text(message, key)
    assert encrypted != message
    decrypted = text_encryptor.decrypt_text(encrypted, key)
    assert decrypted == message


def test_encrypt_decrypt_file_roundtrip(tmp_path: Path):
    plain = tmp_path / "plain.txt"
    enc = tmp_path / "enc.txt"
    dec = tmp_path / "dec.txt"
    plain.write_text("Sample Text", encoding="utf-8")

    assert text_encryptor.encrypt_text_file(str(plain), "key", str(enc))
    assert text_encryptor.decrypt_text_file(str(enc), "key", str(dec))
    assert dec.read_text(encoding="utf-8") == "Sample Text"

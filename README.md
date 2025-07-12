# Simple Encryptor

Utilities for hiding messages or files in PNG images and for encrypting text with a repeating key.

## Installation

```bash
pip install -r requirements.txt
```

## Command Line Usage

The `cli.py` script exposes the functionality via subcommands:

```
python cli.py hide-message <image> <message> <key> <output>
python cli.py decode-message <image> <key>
python cli.py hide-file <image> <file> <key> <output>
python cli.py decode-file <image> <output>
python cli.py encrypt-text <text> <key>
python cli.py decrypt-text <text> <key>
python cli.py encrypt-file <input> <key> <output>
python cli.py decrypt-file <input> <key> <output>
```

## Running Tests

Run `pytest` to execute the unit tests:

```bash
pytest
```

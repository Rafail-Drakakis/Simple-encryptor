import argparse
import image_encryptor
import text_encryptor


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple Encryptor command line")
    subparsers = parser.add_subparsers(dest="command", required=True)

    hide_msg = subparsers.add_parser("hide-message", help="Hide a text message in an image")
    hide_msg.add_argument("image", help="Input image file")
    hide_msg.add_argument("message", help="Message to hide")
    hide_msg.add_argument("key", help="Encryption key")
    hide_msg.add_argument("output", help="Output encoded image")

    decode_msg = subparsers.add_parser("decode-message", help="Decode a message from an image")
    decode_msg.add_argument("image", help="Encoded image file")
    decode_msg.add_argument("key", help="Decryption key")

    hide_file = subparsers.add_parser("hide-file", help="Hide a file in an image")
    hide_file.add_argument("image", help="Input image file")
    hide_file.add_argument("file", help="File to hide")
    hide_file.add_argument("key", help="Encryption key")
    hide_file.add_argument("output", help="Output encoded image")

    decode_file = subparsers.add_parser("decode-file", help="Extract a file from an image")
    decode_file.add_argument("image", help="Encoded image")
    decode_file.add_argument("output", help="Output file path")

    enc_text = subparsers.add_parser("encrypt-text", help="Encrypt a text string")
    enc_text.add_argument("text", help="Plain text")
    enc_text.add_argument("key", help="Encryption key")

    dec_text = subparsers.add_parser("decrypt-text", help="Decrypt a text string")
    dec_text.add_argument("text", help="Cipher text")
    dec_text.add_argument("key", help="Decryption key")

    enc_file = subparsers.add_parser("encrypt-file", help="Encrypt a text file")
    enc_file.add_argument("input", help="Input file path")
    enc_file.add_argument("key", help="Encryption key")
    enc_file.add_argument("output", help="Output encrypted file")

    dec_file = subparsers.add_parser("decrypt-file", help="Decrypt a text file")
    dec_file.add_argument("input", help="Input encrypted file")
    dec_file.add_argument("key", help="Decryption key")
    dec_file.add_argument("output", help="Output decrypted file")

    args = parser.parse_args()

    if args.command == "hide-message":
        if image_encryptor.hide_message_in_png(args.image, args.message, args.key, args.output):
            print("Message hidden successfully")
    elif args.command == "decode-message":
        message = image_encryptor.decode_message_from_png(args.image, args.key)
        print(message)
    elif args.command == "hide-file":
        if image_encryptor.hide_file_in_png(args.image, args.file, args.key, args.output):
            print("File hidden successfully")
    elif args.command == "decode-file":
        result = image_encryptor.decode_file_from_png(args.image, args.output)
        if result:
            print(result)
    elif args.command == "encrypt-text":
        print(text_encryptor.encrypt_text(args.text, args.key))
    elif args.command == "decrypt-text":
        print(text_encryptor.decrypt_text(args.text, args.key))
    elif args.command == "encrypt-file":
        if text_encryptor.encrypt_text_file(args.input, args.key, args.output):
            print(f"File encrypted and saved as {args.output}")
    elif args.command == "decrypt-file":
        if text_encryptor.decrypt_text_file(args.input, args.key, args.output):
            print(f"File decrypted and saved as {args.output}")


if __name__ == "__main__":
    main()

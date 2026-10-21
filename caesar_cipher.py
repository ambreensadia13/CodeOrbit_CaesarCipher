
def caesar_cipher(message, shift, mode):
    """Encrypt or decrypt a message using a Caesar cipher."""

    if mode == "decrypt":
        shift = -shift

    result = ""

    for char in message:
        if char.isupper():
            base = ord("A")
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)

        elif char.islower():
            base = ord("a")
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)

        else:
            # Preserve spaces, digits, and punctuation.
            result += char

    return result


def main():
    print("=" * 42)
    print("       CAESAR CIPHER ENCRYPTION TOOL")
    print("=" * 42)

    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "3":
            print("Thank you for using Caesar Cipher Tool!")
            break

        if choice not in ("1", "2"):
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        message = input("Enter your message: ")

        try:
            shift = int(input("Enter the shift key: "))
        except ValueError:
            print("Invalid shift key. Please enter a whole number.")
            continue

        if choice == "1":
            result = caesar_cipher(message, shift, "encrypt")
            print("\nEncrypted message:", result)

        else:
            result = caesar_cipher(message, shift, "decrypt")
            print("\nDecrypted message:", result)

        print("\nNote: Caesar cipher is for educational use only.")


if __name__ == "__main__":
    main()

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text


def main():
    while True:
        print("Caesar Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
        print()


if __name__ == "__main__":
    main()

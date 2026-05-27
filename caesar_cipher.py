def caesar_encrypt(text, shift):
    encrypted_text = ""
    shift = shift % 26
    
    for char in text:
        if char.isupper():
            encrypted_char = chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_char = chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    
    return encrypted_text


def caesar_decrypt(text, shift):
    decrypted_text = ""
    shift = shift % 26
    
    for char in text:
        if char.isupper():
            decrypted_char = chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_char = chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    
    return decrypted_text


def get_valid_shift():
    while True:
        try:
            shift = int(input("Enter shift key (integer): "))
            return shift
        except ValueError:
            print("Error: Please enter a valid integer!")


def main():
    while True:
        print("\n" + "="*50)
        print("          CAESAR CIPHER - ENCRYPTION & DECRYPTION          ")
        print("="*50)
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            print("\n--- ENCRYPTION MODE ---")
            original_text = input("Enter text to encrypt: ")
            shift = get_valid_shift()
            encrypted_text = caesar_encrypt(original_text, shift)
            
            print("\n" + "-"*50)
            print(f"Original Text   : {original_text}")
            print(f"Shift Key       : {shift}")
            print(f"Encrypted Text  : {encrypted_text}")
            print("-"*50)
        
        elif choice == "2":
            print("\n--- DECRYPTION MODE ---")
            encrypted_text = input("Enter text to decrypt: ")
            shift = get_valid_shift()
            decrypted_text = caesar_decrypt(encrypted_text, shift)
            
            print("\n" + "-"*50)
            print(f"Encrypted Text  : {encrypted_text}")
            print(f"Shift Key       : {shift}")
            print(f"Decrypted Text  : {decrypted_text}")
            print("-"*50)
        
        elif choice == "3":
            print("\nThank you for using Caesar Cipher! Goodbye!")
            break
        
        else:
            print("\nError: Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

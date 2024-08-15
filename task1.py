def encrypt_caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
            elif char.isupper():
                start = ord('A')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar_cipher(text, shift):
    return encrypt_caesar_cipher(text, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption")
    action = input("Would you like to (E)ncrypt or (D)ecrypt? ").upper()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (integer): "))
    
    if action == 'E':
        encrypted_message = encrypt_caesar_cipher(message, shift)
        print("Encrypted message:", encrypted_message)
    elif action == 'D':
        decrypted_message = decrypt_caesar_cipher(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid action. Please choose 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()

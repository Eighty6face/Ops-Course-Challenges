#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 6
# Author:                        Alex Wise
# Date of latest revision:       01/23/2023
# Purpose:                       Encrption

# task
    #  create a script that utilizes the cryptography library to:
        # Prompt the user to select a mode
            # Encrypt a file (mode 1)
            # Decrypt a file (mode 2) 
            # Encrypt a message (mode 3)
            # Decrypt a message (mode 4)
        
        # If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
        # If mode 3 or 4 are selected, prompt the user to provide a cleartext string.

        # few errors coming up I dont understand 

# Import Libraries
from cryptography.fernet import Fernet

# Define Functions
#Fern Class
# initialize the Fernet class
f = Fernet(key)

# Key Gen
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
key_file.write(key)

# write Gen Key
def load_key():
    return open ("key.key", "rb").read()

write_key()

f = Fernet(key)
key = load_key()
print("Key is " + str(key.decode('utf-8')))

  


# Encrypt file
def encrypt_file():
    file = user_path.encode()
    encrypted_file = f.encrypt(file)
    print("Decrypted file is " + str(encrypted_file.decode('utf-8')))

# Decrypts file
def decrypt_file():
    file = user_path.encode()
    decrypted_file = f.decrypt(file)
    print("Encrypted file is " + str(decrypted_file.decode('utf-8')))

# Encrypts Msg
def encrypt_message():
    message = user_msg.encode()
    encrypted_message = f.encrypt(message)
    print("Ciphertext is " + str(encrypted_message.decode('utf-8')))

# Decrypts Msg
def decrypt_message():
    message = user_msg.encode()
    decrypted_message = f.decrypt(message)
    print("Plaintext is " + str(decrypted_message.decode('utf-8')))



#infinte loop 
def ask-user():
print ("Please make your selection:")
mode = input("\nWelcoem to the encryption menu. What would you like? \n1. Mode 1- Encrypt a file\n2. Mode 2- Decrypt a file\n3. Mode 3- Encrypt a message\n4. Mode 4- Decrypt a message")

if  (mode == "1"):
    encrypt_file()
    print("Your file was encrypted ")
elif (mode == "2")
    decrypt_file()
    print("Your file was decrypted ")
elif (mode == "3")
    encrypt_message()
    print("Your message was encrypted ")
elif (mode == "4")
    decrypt_message()
    print("Your message was decrypted ")
else:
    print("Please make another selection")


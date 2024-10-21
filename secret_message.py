encryption_key = {
    "0": "A",
    "1": "S",
    "2": "D",
    "3": "F",
    "4": "G",
    "5": "H",
    "6": "J",
    "7": "K",
    "8": "L",
    "9": "Z",
    " ": "Q"
}

decryption_key = {
    "A": "0",
    "S": "1",
    "D": "2",
    "F": "3",
    "G": "4",
    "H": "5",
    "J": "6",
    "K": "7",
    "L": "8",
    "Z": "9",
    "Q": " "
}

def encrypt_string(string):    
    encrypted_string = ""

    for letter in string:
        if letter in encryption_key:
            encrypted_string += encryption_key[letter]
        else:
            encrypted_string += letter

    return encrypted_string

def decrypt_string(encrypted_string):
    decrypted_string = ""

    decryption_keys = list(encryption_key.keys())
    for letter in encrypted_string:
        decrypted_letter = decryption_keys[ list(encryption_key.values()).index(letter) ]
        decrypted_string += decrypted_letter

    return decrypted_string

action = ""
while action == "":
    action = input("Select 1 to Encrypt or 2 to Decrypt: ")


if action == "1":
    plain_string = input("Enter the text to encrypt: ")
    print(encrypt_string(plain_string))
elif action == "2":
    encrypted_string = input("Enter the string you want to decrypt: ")
    print(decrypt_string(encrypted_string))
else:
    print("This action is invalid. Please run the program again and select a valid option")
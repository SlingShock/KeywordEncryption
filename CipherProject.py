import string
import random

# Initial values
ascii_mapping = {chr(i): i-32 for i in range(32, 127)}
for char, value in ascii_mapping.items():
    print(f"'{char}': {value}")

# Function for generating a random keyword
def generate_random_keyword(min_length=32, max_length=64):
    length = random.randint(min_length, max_length)
    characters = string.ascii_letters + string.digits + string.punctuation
    keyword =  ''.join(random.choice(characters) for _ in range(length))
    return keyword

# Function that converts a number to a letter string
def number_to_letter(number):
    number = number % 95
    result = chr(number+32)
    return result

# Function that returns true if a string is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Function for generating a keyword for encryption/decryption
def keyword_generation():
    while True:

        keyword = ''

        print("1. Generate random keyword")
        print("2. Choose your own keyword")
        print("3. Cancel")
        key_choice = input()
        key_choice = int(key_choice)

        if key_choice == 1:
            keyword = generate_random_keyword()
            return keyword
        elif key_choice == 2:
            keyword = input("Enter a keyword: ")
            return keyword
        elif key_choice == 3:
            print("Canceling...")
            return keyword
        else: 
            print("Invalid Option")

# Function for setting the length of the keyword to the length of the text
def keyword_adjustment(keyword, plaintext_length, keyword_length):
    
    encryption_keyword = keyword
    while (plaintext_length != keyword_length):

        if keyword_length > plaintext_length:
            encryption_keyword = encryption_keyword[:len(plaintext)]
        elif keyword_length < plaintext_length:
            encryption_keyword += encryption_keyword

        plaintext_length = len(plaintext)
        keyword_length = len(encryption_keyword)
    
    return encryption_keyword
    

# Encryption function
def encryption(plaintext, keyword): 

    plaintext_length = len(plaintext)
    keyword_length = len(keyword)

    encryption_keyword = keyword_adjustment(keyword, plaintext_length, keyword_length)

    encrypted_text = ''

    for i in range (plaintext_length):
        letter = plaintext[i]
        value = ascii_mapping[letter]
        
        key_letter = encryption_keyword[i]
        key_value = ascii_mapping[key_letter]

        encrypted_value = value + key_value
        
        encrypted_letter = number_to_letter(encrypted_value)

        encrypted_text = encrypted_text + encrypted_letter

        for i in range (key_value + 1):
            next_value = random.randint(1, 94)
            next_letter = number_to_letter(next_value)
            encrypted_text = encrypted_text + next_letter
        
    return encrypted_text

# Decryption funciton
def decryption(encrypted_text, keyword):
    
    encrypted_length = len(encrypted_text)
    keyword_length = len(keyword)

    decryption_keyword = keyword_adjustment(keyword, encrypted_length, keyword_length)

    decrypted_text = ''
    while encrypted_text != '':
        encryption_length = len(encrypted_text)
        
        encrypted_letter = encrypted_text[0]
        encrypted_value = ascii_mapping[encrypted_letter]

        key_letter = decryption_keyword[0]
        key_value = ascii_mapping[key_letter]
            
        decrypted_value = encrypted_value - key_value
            
        decrypted_letter = number_to_letter(decrypted_value)

        decrypted_text = decrypted_text + decrypted_letter

        encrypted_text = encrypted_text[1:]
        deletion_value = key_value + 1
        encrypted_text = encrypted_text[deletion_value:encryption_length]
        decryption_keyword = decryption_keyword[1:]

    return decrypted_text

# Function calling 
plaintext = input("Enter plaintext: ")
keyword = keyword_generation()

print("Plaintext: " + plaintext)
print("Keyword: " + keyword)

encrypted_text = encryption(plaintext, keyword)
print("Encrypted Text: " + encrypted_text)

decrypted_text = decryption(encrypted_text, keyword)
print("Decrypted Text: "+ decrypted_text)

import random
import string

def generate_password(length):
    # Define the characters to use in the password
    special_characters = "!@#$%^&*()"
    all_characters = string.ascii_letters + string.digits + special_characters

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
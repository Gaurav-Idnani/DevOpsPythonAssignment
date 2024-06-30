# Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength. 
# Implement a Python function called check_password_strength that takes a password string as input.
# The function should check the password against the following criteria:
# Minimum length: The password should be at least 8 characters long.
# Contains both uppercase and lowercase letters.
# Contains at least one digit (0-9).
# Contains at least one special character (e.g., !, @, #, $, %).
# The function should return a boolean value indicating whether the password meets the criteria.
# Write a script that takes user input for a password and calls the check_password_strength function to validate it.
# Provide appropriate feedback to the user based on the strength of the password.  


import re

def check_password_strength(password):
    
    # Checks the password meets for the following criteria:
    # - Minimum length: 8 characters.
    # - Contains both uppercase and lowercase letters.
    # - Contains at least one digit (0-9).
    # - Contains at least one special character (e.g., !, @, #, $, %).
    # return true if all criteria fulfilled otherwise false.
    
    if len(password) < 8:
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'[0-9]', password):
        return False
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True

def callPasswordCheck():
    
    # function to take user input and validate the password.
    
    password = input("Enter a password to check strength: ")
    if check_password_strength(password):
        print("Password entered is strong as it matches all criteria")
    else:
        print("")
        print("Password entered is weak. It needs to fulfill the following criteria.")
        print("-Password entered should be at least 8 characters long")
        print("-Password entered should contains both uppercase and lowercase letters")
        print("-Password entered should have at least one digit, and at least one special character.")

callPasswordCheck()



# Password Strength Checker & Generator (CLI)

import re
import random
import string

def has_number(password):
    return bool(re.search(r'\d', password))

def has_upper(password):
    up = False
    for i in password:
        if i.isupper():
            up = True
            break
    return up

def has_special_char(password):
    special_char = False
    for char in password:
        if not char.isalpha() and not char.isdigit():
            special_char = True
            break
    return special_char

def check_strength(password):
    length = len(password)
    has_num = has_number(password)
    has_up = has_upper(password)
    has_spc_char = has_special_char(password)
    score = 0

    if length > 8:
        score += 1 
    if has_num:
        score +=1
    if has_up:
        score += 1
    if has_spc_char:
        score += 1
    return score

def check_score(score):
    if score <= 1:
        return "Your password is Weak."
    elif score in range(2, 4):
        return "Your password is Mid."
    else:
        return "Your password is Strong."
    
def generate_password(length=15):
    all_chars = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    while True:
        password = "".join(random.choice(all_chars) for _ in range(length))
        strong_password = check_strength(password)
        if strong_password >= 4:
            return password
            

def main():
    password = input("Enter your password: ")
    score = check_strength(password)
    result = check_score(score)
    print(result)
    
    if score < 4:
        choice = input("Do you want me to generate a stronger password? (y/n): ").lower()

        if choice == "y":
            print("Generated strong password:", generate_password())

main()
    
    

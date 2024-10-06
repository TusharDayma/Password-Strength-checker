import re

def password_strength(password):
    # Password length
    length = len(password)
    
    # Check for different character types
    has_lower = re.search(r'[a-z]', password) is not None
    has_upper = re.search(r'[A-Z]', password) is not None
    has_digit = re.search(r'[0-9]', password) is not None
    has_special = re.search(r'[\W_]', password) is not None
    
    # Evaluate strength
    score = 0
    if length >= 8:
        score += 1
    if has_lower:
        score += 1
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    # Strength evaluation
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    else:
        return "Weak"

# Input password from the user
password = input("Enter a password to check its strength: ")
print(f"Password Strength: {password_strength(password)}")

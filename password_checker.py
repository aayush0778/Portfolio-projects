import random
import string

def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    
    if score >= 4:
        return "Strong"
    elif score >= 2:
        return "Medium"
    else:
        return "Weak"

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

password = input("Enter a password to check: ")
strength = check_strength(password)
print(f"Password strength: {strength}")

if strength == "Weak":
    print("Suggestion: Use a stronger one!")
    generated = generate_password()
    print(f"Generated strong password: {generated}")
elif strength == "Medium":
    print("Tip: Add more variety for better security.")
else:
    print("Great job! It's strong.")

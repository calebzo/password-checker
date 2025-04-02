import re

def check_password_strength(password):
    # Check length
    if len(password) < 6:
        return "❌ Very Weak: Password is too short!"
    elif len(password) < 10:
        return "⚠️ Weak: Make it at least 10 characters long."

    # Check complexity
    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_digit = re.search(r"\d", password)
    has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    if has_upper and has_lower and has_digit and has_special:
        return "✅ Strong: Your password is secure!"
    else:
        return "⚠️ Medium: Add uppercase, numbers, and special characters for strength."

# User input
password = input("Enter a password to check: ")
print(check_password_strength(password))

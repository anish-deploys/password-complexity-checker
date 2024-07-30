import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Criteria
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Assess strength
    if length_criteria:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if upper_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if lower_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if number_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    if special_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one special character (e.g., !, @, #, $).")

    # Determine overall strength
    if strength == 5:
        strength_feedback = "Strong"
    elif strength >= 3:
        strength_feedback = "Moderate"
    else:
        strength_feedback = "Weak"

    return strength_feedback, feedback

# Example usage
password = input("Enter a password to assess: ")
strength_feedback, feedback = assess_password_strength(password)
print(f"Password Strength: {strength_feedback}")
for comment in feedback:
    print(comment)
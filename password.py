import random 
import string

def generate_password(length=8, use_upper=True, use_lower=True, use_digits=True):
    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits

    if not chars:
        raise ValueError("At least one character type should be selected.")
    return "".join(random.choice(chars) for _ in range(length))

def get_bool_input(prompt):
        while True:
            user_input = input(prompt).strip().lower()
            if user_input == "y":
                return True
            elif user_input == "n":
                return False
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
def get_legth_input(prompt):
    while True:
        length_input = input(prompt)
        if length_input.isdigit():
            return int(length_input)
        else:
            print("Invalid input. Please enter a number")

def evaluate_password_strength(password):
    if len(password) <= 15:
        return "Weak"
    elif len(password) <= 35:
        return "Medium"
    else:
        return "Strong"

def main():
    length = get_legth_input("Enter the length of the password: ")
    use_upper = get_bool_input("Include uppercase letters? (Y/N): ")
    use_lower = get_bool_input("Include lowercase letters? (Y/N): ")
    use_digits = get_bool_input("Include digits? (Y/N): ")

    password = generate_password(length, use_upper, use_lower, use_digits)
    print("Generated password:", password)
    print("Password strength:", evaluate_password_strength(password))
if __name__ == "__main__":
    main()
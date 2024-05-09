import random
class PasswordGenerator:
    def __init__(self, length) -> None:
        self.length = length
        self.characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

    
    # Function to generate a random password
    def generate_password(self):
        password = ''.join(random.choice(self.characters) for i in range(self.length))
        return password

    # Function to check password strength
    def check_password_strength(self, password):
        # Define criteria for a strong password
        criteria = {
            'length': len(password) >= 8,
            'lowercase': any(char.islower() for char in password),
            'uppercase': any(char.isupper() for char in password),
            'digit': any(char.isdigit() for char in password),
            'special': any(char in "!@#$%^&*()" for char in password)
        }
        # Count how many criteria are met
        strength = sum(criteria.values())
        return strength

password_generator = PasswordGenerator(12)
# Generate and print a random password of length 12
password = password_generator.generate_password()
print("Generated password:", password)

# Check the strength of the generated password
strength = password_generator.check_password_strength(password)
print("Password strength:", strength)
import string

# Taking input from the user
password = input("Enter the password: ")

# Criteria for password complexity
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

# Collecting all character types
characters = [upper_case, lower_case, special, digits]

# Password length
length = len(password)

# Initial score
score = 0

# Reading common passwords from a file
common_passwords = ['123456', 'password', '123456789', 'qwerty', 'abc123']  # You can replace with an actual file

if password in common_passwords:
    print("Password was found in a common list. Score : 0 / 14")
else:
    # Score based on password length
    if length > 8:
        score += 2
    if length > 12:
        score += 2
    if length > 17:
        score += 2
    if length > 20:
        score += 2
    print(f"Password length is {str(length)}, adding {str(score)} points")

    # Score based on variety of character types
    if sum(characters) > 1:
        score += 2
    if sum(characters) > 2:
        score += 2
    if sum(characters) > 3:
        score += 2
    print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters) - 1)} points!")

    # Final score evaluation
    if score < 4:
        print(f"Password is weak! Score: {str(score)} / 14 ")
    elif score == 4:
        print(f"Password is average! Score: {str(score)} / 14")
    elif 4 < score < 6:
        print(f"Password is good! Score: {str(score)} / 14")
    elif score > 6:
        print(f"Password is strong! Score: {str(score)} / 14")

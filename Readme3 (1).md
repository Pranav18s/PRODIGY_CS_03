
# **PRODIGY_CS_03 - Password Complexity Checker 🔐**

This Python project implements a simple password complexity checker to assess the strength of user-generated passwords based on different factors such as length, inclusion of uppercase and lowercase letters, digits, and special characters. It helps users ensure their passwords are strong enough to protect their data. 🛡️

## ✨ **Features**

- **Length Evaluation**: Scores based on password length, with higher scores for longer passwords. 📏
- **Character Variety Check**: Assesses the presence of uppercase, lowercase letters, digits, and special characters. 🔠🔢
- **Common Password Detection**: Flags commonly used weak passwords for security. 🛑
- **Custom Scoring System**: Generates a complexity score on a scale of 0 to 14. 📊

## 🚀 **How It Works**

### Password Length Scoring

- The password receives points based on its length:
  - More than 8 characters: **+2 points**
  - More than 12 characters: **+2 points**
  - More than 17 characters: **+2 points**
  - More than 20 characters: **+2 points**

### Character Variety Scoring 🔡🔢

- Points are added based on the presence of different types of characters:
  - Uppercase letters: **1 point**
  - Lowercase letters: **1 point**
  - Digits: **1 point**
  - Special characters: **1 point**
  - Additional points are added if more than one character type is present.

### Common Password Detection ⚠️

- If the password is found in a list of common passwords, it automatically receives a score of **0**, regardless of its other characteristics.

### Final Complexity Score

- The password is evaluated based on a **14-point** scale:
  - **Weak**: 0–4 points
  - **Average**: 4 points
  - **Good**: 5–6 points
  - **Strong**: More than 6 points

## 🛠️ **How to Use**

1. Clone the repository:

   ```bash
   git clone https://github.com/Pranav18s/PRODIGY_CS_03.git
   ```

2. Run the script:

   ```bash
   python PasswordComplexityChecker.py
   ```

3. Enter your password when prompted, and the program will evaluate its complexity:

   ```bash
   Enter the password: My$ecureP@ssw0rd!
   Password length is 16, adding 6 points.
   Password has 4 different character types, adding 3 points!
   Password is strong! Score: 9 / 14
   ```

## 👤 **Author**

**Pranav S**  
[www.linkedin.com/in/pranav-s-85b106269](https://www.linkedin.com/in/pranav-s-85b106269)

## 📄 **License**

This project is licensed under the MIT License.

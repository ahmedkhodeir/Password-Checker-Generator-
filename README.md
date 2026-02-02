## Author

Ahmed Khodeir   
Software Developer  

Personal learning project 🚀


# Password Strength Checker & Generator (CLI)

A simple Python command-line tool that checks the strength of a password and can generate a strong password if the entered one is weak or medium.

This project was built as a personal learning project to practice:
- Problem solving
- Clean code structure
- Functions and logic separation
- User interaction via CLI

---

## Features

- Check password strength based on:
  - Length
  - Numbers
  - Uppercase letters
  - Special characters
- Score-based evaluation system
- Clear strength levels:
  - Weak
  - Mid
  - Strong
- Option to generate a strong password automatically
- Guaranteed generated passwords meet all strength criteria

---

## Password Strength Rules

Each condition gives **1 point**:

- Length greater than 8 characters
- Contains at least one number
- Contains at least one uppercase letter
- Contains at least one special character

### Scoring
- **0–1** → Weak  
- **2–3** → Mid  
- **4** → Strong  

---

## How to Run

### Requirements
- Python 3.8+

### Run the program
```bash
python password_checker.py


import re

# Get user details
email = input("Enter email: ")
password = input("Enter password: ")
mobile = input("Enter mobile number: ")

# Email validation
email_pattern = r"^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.(com|org|edu|net|in)$"
if re.fullmatch(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

# Password validation
password_pattern = (
    r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)"
    r"(?=.*[@#$%&!]).{8,}$"
)
if re.fullmatch(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password")

# Mobile number validation
mobile_pattern = r"^[6-9]\d{9}$"
if re.fullmatch(mobile_pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")


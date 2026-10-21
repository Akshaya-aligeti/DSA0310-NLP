
import re

def validate(pattern, value):
    return re.fullmatch(pattern, value) is not None

# Get student details
reg_no = input("Enter register number: ")
email = input("Enter institutional email: ")
course = input("Enter course code: ")
semester = input("Enter semester (1-8): ")
mobile = input("Enter mobile number: ")

# Validation patterns
reg_pattern = r"\d{12}"
email_pattern = r"[a-zA-Z0-9._%+-]+@university\.edu"
course_pattern = r"[A-Z]{2,4}\d{3}"
semester_pattern = r"[1-8]"
mobile_pattern = r"[6-9]\d{9}"

# Validate fields
results = {
    "Register Number": validate(reg_pattern, reg_no),
    "Institutional Email": validate(email_pattern, email),
    "Course Code": validate(course_pattern, course),
    "Semester": validate(semester_pattern, semester),
    "Mobile Number": validate(mobile_pattern, mobile)
}

# Display validation messages
print("\nVALIDATION REPORT")
print("-----------------")

for field, valid in results.items():
    if valid:
        print(field, ": Valid")
    else:
        print(field, ": Invalid")

# Final registration status
if all(results.values()):
    print("\nRegistration Successful")
else:
    print("\nRegistration Failed")


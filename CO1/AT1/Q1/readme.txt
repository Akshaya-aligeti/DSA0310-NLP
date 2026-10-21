
import re

def extract_resume(text):
    # Extract candidate name
    name = re.search(r"Name\s*:\s*([A-Za-z ]+)", text)
    name = name.group(1).strip() if name else "Not found"

    # Extract email
    email = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

    # Extract mobile number
    mobile = re.findall(r'\b\d{10}\b', text)

    # Detect technical skills
    skills_list = ["Python", "Java", "SQL",
                   "Machine Learning", "NLP"]
    skills = [s for s in skills_list
              if re.search(r'\b' + re.escape(s) + r'\b',
                           text, re.I)]

    # Extract years of experience
    exp = re.search(r'(\d+)\s*years?\s+of experience',
                    text, re.I)
    experience = int(exp.group(1)) if exp else 0

    # Check eligibility
    eligible = experience >= 2 and "Python" in skills

    # Display structured profile
    profile = {
        "Name": name,
        "Email": email,
        "Mobile": mobile,
        "Skills": skills,
        "Experience": experience,
        "Eligible": eligible
    }

    return profile


# Sample resume data
resumes = [
    """Name: Arun Kumar
    Email: arun@gmail.com
    Mobile: 9876543210
    Skills: Python, Java, SQL
    3 years of experience""",

    """Name: Priya Sharma
    Email: priya@gmail.com
    Mobile: 9123456780
    Skills: Java, NLP
    1 year of experience"""
]

# Process resumes
for resume in resumes:
    profile = extract_resume(resume)
    print(profile)


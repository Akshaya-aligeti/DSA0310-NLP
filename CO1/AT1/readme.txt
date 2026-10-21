
import re

def extract_resume(text):
    # Extract name
    match = re.search(r"Name:\s*([A-Za-z ]+)", text)
    name = match.group(1).strip() if match else "Not found"

    # Extract email
    email = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)

    # Extract mobile number
    mobile = re.findall(r"\b\d{10}\b", text)

    # Extract technical skills
    skill_list = ["Python", "Java", "SQL",
                  "Machine Learning", "NLP"]

    skills = []
    for skill in skill_list:
        if re.search(r"\b" + re.escape(skill) + r"\b",
                     text, re.I):
            skills.append(skill)

    # Extract experience
    match = re.search(
        r"(\d+)\s*years?\s+of experience", text, re.I
    )
    experience = int(match.group(1)) if match else 0

    # Check eligibility
    eligible = experience >= 2 and "Python" in skills

    # Return structured profile
    return {
        "Name": name,
        "Email": email,
        "Mobile": mobile,
        "Skills": skills,
        "Experience": experience,
        "Eligible": eligible
    }


# Sample resume
resume = """
Name: Arun Kumar
Email: arun@gmail.com
Mobile: 9876543210
Skills: Python, Java, SQL
3 years of experience
"""

profile = extract_resume(resume)

# Display candidate details
print("CANDIDATE PROFILE")
print("-----------------")

for key, value in profile.items():
    print(key, ":", value)


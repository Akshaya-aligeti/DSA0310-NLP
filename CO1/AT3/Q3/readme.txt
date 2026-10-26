
import re

text = input("Enter text: ")

while True:
    print("\n1. Search Word")
    print("2. Search Date")
    print("3. Search Phone Number")
    print("4. Search Hashtag")
    print("5. Search Mention")
    print("6. Search Prefix")
    print("7. Search Suffix")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        word = input("Enter word: ")
        pattern = r"\b" + re.escape(word) + r"\b"

    elif choice == "2":
        pattern = r"\b\d{2}/\d{2}/\d{4}\b"

    elif choice == "3":
        pattern = r"\b[6-9]\d{9}\b"

    elif choice == "4":
        pattern = r"(?<!\w)#[A-Za-z0-9_]+"

    elif choice == "5":
        pattern = r"(?<!\w)@[A-Za-z0-9_]+"

    elif choice == "6":
        prefix = input("Enter prefix: ")
        pattern = r"\b" + re.escape(prefix) + r"\w*"

    elif choice == "7":
        suffix = input("Enter suffix: ")
        pattern = r"\w*" + re.escape(suffix) + r"\b"

    elif choice == "8":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
        continue

    matches = re.findall(pattern, text, re.I)

    if matches:
        print("Matching patterns:", matches)
        print("Total matches:", len(matches))
    else:
        print("No matching patterns found")


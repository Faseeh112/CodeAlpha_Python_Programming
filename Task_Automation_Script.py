import re

def extract_emails():
    input_file = "input.txt"
    output_file = "emails.txt"

    with open(input_file, "r") as f:
        content = f.read()

    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", content)

    with open(output_file, "w") as f:
        for email in emails:
            f.write(email + "\n")

    print(f"✅ Extracted {len(emails)} email(s) saved to {output_file}")

if __name__ == "__main__":
    extract_emails()

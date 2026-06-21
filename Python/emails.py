import requests
import re

url = "https://www.yell.ge/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    html = response.text

    # Extract email addresses
    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        html
    )

    # Remove duplicates
    emails = sorted(set(emails))

    print("Found emails:")
    for email in emails:
        print(email)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
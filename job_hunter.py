import requests
import smtplib
import os
from email.mime.text import MIMEText

KEYWORDS = [
    "spring boot",
    "java",
    "react",
    "full stack",
    "ai",
    "machine learning"
]

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

def get_jobs():

    url = "https://remotive.com/api/remote-jobs"
    data = requests.get(url).json()

    results = []

    for job in data["jobs"]:

        title = job["title"].lower()

        if any(skill in title for skill in KEYWORDS):

            results.append(
                f"{job['title']} - {job['company_name']}\n{job['url']}\n"
            )

    return results[:10]


def send_email(jobs):

    body = "\n\n".join(jobs)

    msg = MIMEText(body)
    msg["Subject"] = "🚀 Daily Job Alerts"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(EMAIL, PASSWORD)

    server.send_message(msg)

    server.quit()


if __name__ == "__main__":

    jobs = get_jobs()

    send_email(jobs)
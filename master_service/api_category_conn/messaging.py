# importing the requests library
import requests


# Add communication to messaging api category service

def send_email(recipient, subject, content):
    """
    :param String recipient: recipient of the email
    :param String subject: subject of the email
    :param String content: content of the email
    """
    response = requests.post(url="http://127.0.0.1:8000/api/send_email/", json={'recipient': recipient,
                                                                                'subject': subject,
                                                                                'content': content})
    return response.json()["status"]

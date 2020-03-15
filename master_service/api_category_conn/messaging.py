# importing the requests library
from django.contrib.sites import requests

from messaging_constants import MESSAGING_SERVICE_URL, MESSAGING_EMAIL_ENDPOINT ,MESSAGING_PURPOSE_SEND_MAIL

# communication to messaging api category service


def use(messaging_object, last_response):
    if messaging_object['purpose'] == MESSAGING_PURPOSE_SEND_MAIL:
        return send_email(messaging_object)
    elif messaging_object['purpose'] == "ADD FURTHER STUFF HERE":
        return ""


def send_email(messaging_object):
    url = MESSAGING_SERVICE_URL + "" + MESSAGING_EMAIL_ENDPOINT
    post_data = messaging_object
    response = requests.post(url=url, data=post_data)

    # extracting data in json format
    return response.content.json()

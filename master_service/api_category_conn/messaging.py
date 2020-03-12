# importing the requests library
from django.contrib.sites import requests

from ..environment.env import MessagingPurpose, CategoryMessaging

# communication to messaging api category service


def use(messaging_object, last_response):
    if messaging_object['purpose'] == MessagingPurpose.send_mail.value:
        return send_email(messaging_object)
    elif messaging_object['purpose'] == "ADD FURTHER STUFF HERE":
        return ""


def send_email(messaging_object):
    url = CategoryMessaging.url_to_messaging_service.value + "" + CategoryMessaging.uri_to_send_email_function.value
    post_data = messaging_object
    response = requests.post(url=url, data=post_data)

    # extracting data in json format
    return response.content.json()

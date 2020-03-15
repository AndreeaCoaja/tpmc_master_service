import json
import requests
from rest_framework.response import Response
from finance_constants import FINANCE_GET_SPECIFIC_STOCK_PRICE, FINANCE_SERVICE_URL_GET_STOCK_PRICE
import logging


# Maybe delete this function??
# communication to finance api category service based on the purpose of the call
def use(finance_object, last_response):
    if finance_object['purpose'] == FINANCE_GET_SPECIFIC_STOCK_PRICE:
        return get_stockprice_for_company(finance_object)
    elif finance_object['purpose'] == FINANCE_GET_GENERIC_STOCK_PRICE:
        return ""


# actual communication towards finance api category service
def get_stockprice_for_company(finance_object):
    url = FINANCE_SERVICE_URL_GET_STOCK_PRICE
    post_data = json.dumps(finance_object)

    headers = {
        'Content-Type': "application/json"
    }

    response = requests.request("POST", url, headers=headers, data=post_data)

    # extracting data in json format
    return Response(response.json()["stock_price"])

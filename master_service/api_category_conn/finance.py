import json
import requests
from rest_framework.response import Response
from ..constants.constants import FinancePurpose, CategoryFinance
import logging


# Maybe delete this function??
# communication to finance api category service based on the purpose of the call
def use(finance_object, last_response):
    if finance_object['purpose'] == FinancePurpose.get_specific_stockprice.value:
        return get_stockprice_for_company(finance_object)
    elif finance_object['purpose'] == FinancePurpose.get_generic_stockprice.value:
        return ""


# actual communication towards finance api category service
def get_stockprice_for_company(finance_object):
    url = CategoryFinance.url_to_finance_service.value  # + "" + CategoryFinance.uri_to_stock_price_function.value
    post_data = json.dumps(finance_object)
    logging.warning(post_data)

    headers = {
        'Content-Type': "application/json"
    }

    response = requests.request("POST", url, headers=headers, data=post_data)

    logging.warning(response.json())
    # extracting data in json format
    return Response(response.json()["stock_price"])

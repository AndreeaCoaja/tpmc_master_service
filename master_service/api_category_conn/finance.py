import requests
from ..environment.env import FinancePurpose, CategoryFinance
import logging


# communication to finance api category service
def use(finance_object, last_response):
    if finance_object['purpose'] == FinancePurpose.get_specific_stockprice.value:
        return get_stockprice_for_company(finance_object)
    elif finance_object['purpose'] == FinancePurpose.get_generic_stockprice.value:
        return ""


def get_stockprice_for_company(finance_object):
    url = CategoryFinance.url_to_finance_service.value + "" + CategoryFinance.uri_to_stock_price_function.value
    post_data = {finance_object}
    response = requests.post(url=url, data=post_data)

    # extracting data in json format
    return response.content.json()

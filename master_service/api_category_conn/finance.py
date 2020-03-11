import logging

import requests
from requests.models import PreparedRequest


# communication to finance api category service


def get_stockprice_for_company(company):
    url = "url to finance api"
    req = PreparedRequest()
    params = {'company': company}
    req.prepare_url(url, params)

    # sending get request and saving the response as response object
    req = requests.get(url=req.url)

    # extracting data in json format
    logging.info(req.json())
    return req.json()

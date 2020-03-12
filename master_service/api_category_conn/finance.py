import logging

from django.conf.urls import url
from django.contrib.sites import requests

from ..environment import env
from requests.models import PreparedRequest

# communication to finance api category service

requests.post(url="https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail", body={"symbol": "MSFT"})

def get_stockprice_for_company(company):
    req = PreparedRequest()
    params = {'company': company}
    req.prepare_url(url, params)

    # sending get request and saving the response as response object
    req = requests.get(url=req.url)

    # extracting data in json format
    logging.info(req.json())
    return req.json()




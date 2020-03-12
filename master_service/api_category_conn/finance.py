import requests


# communication to finance api category service

def get_stockprice_for_company(company, region="US"):
    response = requests.post(url="http://127.0.0.1:8000/api/stock_price/", json={"symbol": company, "region": region})

    return response.json()["stock_price"]

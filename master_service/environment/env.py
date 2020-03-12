import enum

# environment static variables to keep the code clean and having a single source of truth throughout project


# Messaging Category ENUMS
class CategoryMessaging(enum.Enum):
    url_to_messaging_service = 'http://127.0.0.1:8002/api'
    uri_to_send_email_function = '/send_email'


class MessagingPurpose(enum.Enum):
    send_mail = 'SEND_EMAIL'


# Finance Category ENUMS
class CategoryFinance(enum.Enum):
    url_to_finance_service = 'http://127.0.0.1:8001/api/stock_price/'
    # uri_to_stock_price_function = '/stock_price/'


class FinancePurpose(enum.Enum):
    get_specific_stockprice = 'GET_SPECIFIC_STOCKPRICE'
    get_generic_stockprice = 'GET_GENERIC_STOCKPRICE'


# Collection of all categories
class AllCategoryNames(enum.Enum):
    finance = "FINANCING"
    messaging = "MESSAGING"

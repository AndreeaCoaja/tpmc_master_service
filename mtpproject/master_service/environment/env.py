import enum

# environment static variables to keep the code clean and having a single source of truth throughout project

# Using enum class create enumerations

# Messaging Category
class CategoryMessaging(enum.Enum):
    url_to_aa = 'http://www.url_to_specific_endpoint/endpoint1'
    url_to_bb = 'http://www.url_to_specific_endpoint/endpoint2'


# Finance Category
class CategoryFinance(enum.Enum):
    url_to_stockprice = 'http://www.url_to_specific_endpoint/stockprice'
    url_to_dd = 'http://www.url_to_specific_endpoint/endpoint4'

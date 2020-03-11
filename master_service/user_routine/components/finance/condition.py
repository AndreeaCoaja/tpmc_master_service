import operator
import time

from master_service.api_category_conn import finance
from ..base.condition import Condition


class FinanceCondition(Condition):
    # This variable specifies how often the condition is checked.
    interval_constant = 60

    # The constructors needs the company name as ???? and the Stock price as a real. The relate (relational operator) must be either ">", "<", ">=", "<=", "="
    def __init__(self, id, company_name, stock_price, relate):
        """
        :param int id:
        :param str company_name:
        :param float stock_price:
        :param str relate:
        """
        super().__init__(id, "finance")
        self.company_name = company_name
        self.stock_price = stock_price
        self.relate = relate

    # This function compares the two values with a relational operator which must be either ">", "<", ">=", "<=", "=". It returns true if the statement is true and false if it is false.
    def relation(self, value1, relate, value2):
        """
        :param float value1:
        :param str relate:
        :param float value2:
        :return:
        """
        ops = {'>': operator.gt,
               '<': operator.lt,
               '>=': operator.ge,
               '<=': operator.le,
               '=': operator.eq}
        return ops[relate](value1, value2)

    # This functions gets the stock price from one of the finance category API services
    def get_stock_price(self):
        return finance.get_stockprice_for_company(self.company_name)

    # The activate function checks the stockprice and compares it with the relational operator to the given stockprice.
    # If the relation is satified it breaks and returns ture. If the relation is not satisfied, it will wait "interval_constant" seconds and repeat.
    def activate(self):
        while True:
            if self.relation(self.stock_price, self.relate, self.get_stock_price()):
                break
            time.sleep(self.interval_constant)
        return True

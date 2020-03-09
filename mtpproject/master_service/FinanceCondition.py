import operator
import time

from ConditionClass import Condition


class FinanceCondition(Condition):
    # This variable specifies how often the condition is checked.
    interval_constant = 60

    # The constructors needs the company name as ???? and the Stock price as a real. The relate (relational operator) must be either ">", "<", ">=", "<=", "="
    def __init__(self, company_name, stock_price, relate):
        self.company_name = company_name
        self.stock_price = stock_price
        self.relate = relate

    # This function compares the two values with a relational operator which must be either ">", "<", ">=", "<=", "=". It returns true if the statement is true and false if it is false.
    def relation(value1, relate, value2):
        ops = {'>': operator.gt,
               '<': operator.lt,
               '>=': operator.ge,
               '<=': operator.le,
               '=': operator.eq}
        return ops[relate](value1, value2)

    # This functions gets the stock price from one of the finance category API services
    def get_stock_price(company_name):
        return finance.get_stockprice_for_company(company_name)

    # The activate function checks the stockprice and compares it with the relational operator to the given stockprice.
    # If the relation is satified it breaks and returns ture. If the relation is not satisfied, it will wait "interval_constant" seconds and repeat.
    def activate(self):
        while (True):
            if self.relation(self.stock_price, self.relate, self.get_stock_price(self.company_name)): break
            time.sleep(self.interval_constant)
        return True

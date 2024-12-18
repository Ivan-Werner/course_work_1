import os
import json
import pandas as pd
from datetime import datetime, timedelta

from openpyxl.styles.builtins import currency

from src.utils import main_list, cards_list, total_spent, top_transactions
from utils import main_list, numcards_list, spent, cashback, currency_price, currencies, stock_api

from config import DATA_DIR, operations_path_xlsx



# from src.utils import  spent, cashback, cards_list, main_list

# currency_list = currency_price(currencies(main_list))



def greetings():
    """выводит привествие пользователя в зависимости от времени суток"""
    current_date = datetime.now()
    current_date += timedelta(hours=1)
    # print(current_date.hour)
    if current_date.hour > 4 and current_date.hour <= 12:
        greet = "Доброе утро!"
    elif current_date.hour > 12 and current_date.hour <= 18:
        greet = "Добрый день!"
    elif current_date.hour > 18 and current_date.hour <= 0:
        greet = "Добрый вечер!"
    else:
        greet = "Доброй ночи!"
    return greet

# main_list = xlsx_reading(operations_path_xlsx)



def res_output(greeting, num_list, spent_list, cashback_list, top_transaction_list, currency_list, stock_list):
    res = {}
    cards_list = []
    res["greeting"] = greeting
    for i in range(len(num_list)):
        card_dict = {}
        card_dict["last_digits"] = num_list[i][1:]
        card_dict["total_spent"] = spent_list[i]
        card_dict["cashback"] = cashback_list[i]
        cards_list.append(card_dict)
    res["cards"] = cards_list

    res["top_transactions"] = top_transaction_list

    res["currency_rates"] = currency_list

    res["stock_prices"] = stock_list

    return json.dumps(res, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # print(greetings())
    # print(currency_price(main_list))
    print(res_output(greetings(), numcards_list(main_list), spent(main_list, cards_list), cashback(total_spent), top_transactions(main_list), currency_price(currencies(main_list)), stock_api()))
    # print(top_transactions(main_list))
    # print(stock_api())
    # for i in stock_api():
    #     print(i)
    # print(currencies(main_list))
    # print(main_list)





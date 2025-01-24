import json
import os
from datetime import datetime, timedelta

import pandas as pd


def greetings() -> str:
    """Функция, которая возвращает строку с приветствием в зависимости от времени."""
    hour = int(datetime.now().strftime('%H'))
    if 6 <= hour <= 12:
        return 'Доброе утро!'
    elif 13 <= hour <= 17:
        return 'Добрый день!'
    elif 18 <= hour <= 23:
        return 'Добрый вечер!'
    else:
        return 'Доброй ночи!'


# main_list = xlsx_reading(operations_path_xlsx)


def res_output(greeting, num_list, spent_list, cashback_list, top_transaction_list, currency_list, stock_list):
    """Функция осуществляет вывод общей информации по банковским транзакциям"""
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
    print(greetings())
    # print(currency_price(main_list))
    # print(res_output(greetings(), numcards_list(main_list), spent(main_list, cards_list),
    # cashback(total_spent), top_transactions(main_list), currency_price(currencies(main_list)), stock_api()))
    # print(top_transactions(main_list))
    # print(stock_api())
    # for i in stock_api():
    #     print(i)
    # print(currencies(main_list))
    # print(main_list)

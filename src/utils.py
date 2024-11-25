import os
import json
from http.client import responses

import requests
from datetime import datetime, timedelta

import pandas as pd
from config import DATA_DIR, operations_path_xlsx
from dotenv import load_dotenv
from views import xlsx_reading, numcards_list, main_list

load_dotenv('../.env')

cards_list = numcards_list(main_list)
main_list = xlsx_reading(operations_path_xlsx)

def spent(main_list, cards_list):
    """Высчитывает общую сумму расходов по карте"""
    sum_spent = 0
    spent_list = []
    for num in cards_list:
        for rec in main_list:
            if rec["Номер карты"] == num:
                sum_spent += rec["Сумма операции"]
                sum_spent = round(sum_spent)
        spent_list.append(sum_spent * (-1))
    return spent_list

total_spent = spent(main_list, cards_list)

def cashback(total_spent):
    """Высчитывается кэщбэк"""
    cashback_list = [x / 100 for x in total_spent]
    return cashback_list


def top_transactions(main_list):
    """Выводит топ-5 транзакций"""
    transactions_list = []
    for i in main_list:
        transactions_list.append(i["Сумма платежа"])
        sorted_transaction_list = sorted(transactions_list, reverse=True)

    return sorted_transaction_list[:5]


def stock_api():
    """Получает по API курсы акций и записывает их в список"""
    url = 'https://www.alphavantage.co/query?function=REALTIME_BULK_QUOTES&symbol=MSFT,AAPL,IBM&apikey=demo'
    token = os.getenv("API_KEY_stocks")
    headers = {"apikey" : token}
    response = requests.get(url, headers=headers)
    r = requests.get(url)
    data = r.json()
    res = []
    for i in data['data']:
        stock_dict = {}
        stock_dict['stock'] = i['symbol']
        stock_dict['price'] = i['open']
        res.append(stock_dict)
    return res


def currencies(main_list: list) -> list:
    """Определяем какие валюты присутствуют в нашем файле"""
    currency_list = []
    for i in main_list:
        if i["Валюта операции"] != "RUB":
            currency_list.append(i["Валюта операции"])
    currency_list = list(set(currency_list))
    return currency_list


def currency_price(currency_list):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1"
    token = os.getenv("API_KEY_currency")
    headers = {"apikey" : token}
    res = []
    for i in currency_list:
        currency_dict = {}
        response = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={i}&amount=1", headers=headers)
        data = response.json()
        currency_dict["currency"] = i
        currency_dict["price"] = round(data["info"]["rate"], 2)
        res.append(currency_dict)
    return res






if __name__ == '__main__':
    # print(spent(main_list, cards_list))
    # print(cashback(total_spent))
    # print(top_transactions(main_list))
    # print(stock_api())
    # print(currencies(main_list))
    print(currency_price(currencies(main_list)))





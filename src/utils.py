import os
import json
import requests
from datetime import datetime, timedelta

import pandas as pd
from config import DATA_DIR, operations_path_xlsx
from dotenv import load_dotenv
from views import xlsx_reading, numcards_list, main_list

load_dotenv('.env')

cards_list = numcards_list(main_list)

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
    url = 'https://www.alphavantage.co/query?function=REALTIME_BULK_QUOTES&symbol=MSFT,AAPL,IBM&apikey=demo'
    token = os.getenv("API_KEY")
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




if __name__ == '__main__':
    # print(spent(main_list, cards_list))
    # print(cashback(total_spent))
    print(top_transactions(main_list))
    print(stock_api())




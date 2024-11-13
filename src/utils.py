import os
import json
from datetime import datetime, timedelta

import pandas as pd
from config import DATA_DIR, operations_path_xlsx
from views import xlsx_reading, numcards_list, main_list

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


        

if __name__ == '__main__':
    print(spent(main_list, cards_list))
    print(cashback(total_spent))



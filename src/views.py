import os
import json
from datetime import datetime, timedelta

import pandas as pd
from config import DATA_DIR, operations_path_xlsx


def xlsx_reading(operations_path_xlsx: str):
    """Преобразует XLSX-файл в список словарей"""
    try:
        py_file = pd.read_excel(operations_path_xlsx)
        py_dict = py_file.to_dict(orient='records')
        return py_dict
    except Exception:
        return []

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

main_list = xlsx_reading(operations_path_xlsx)

def numcards_list(main_list: list) -> list:
    """Выводит список маскированных номеров карт"""
    res_list = []
    for i in main_list:
        if (i["Номер карты"] not in res_list) and type(i["Номер карты"]) == str:
            elem = (i["Номер карты"])
            res_list.append(elem)
    # num_list = []
    # for elem in res_list:
    #     num_list.append(elem[1:])

    return res_list






if __name__ == '__main__':
    print(greetings())
    # print(xlsx_reading(operations_path_xlsx))
    print(numcards_list(main_list))








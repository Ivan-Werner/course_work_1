import os
import json
from http.client import responses
import re

import requests
from datetime import datetime, timedelta

import pandas as pd
from config import DATA_DIR, operations_path_xlsx
from dotenv import load_dotenv
from utils import xlsx_reading, numcards_list, main_list

def simple_search(main_list):
    """Функция реализует поиск по ключам Категория и Описание"""
    pattern = input("Найти: ")
    res = []
    for i in main_list:
        if (type(i["Категория"]) == str) and (re.findall(pattern, i["Категория"], flags=re.IGNORECASE)) or (re.findall(pattern, i["Описание"], flags=re.IGNORECASE)):
            res.append(i)
    return res


if __name__ == '__main__':
    s = simple_search(main_list)
    # for i in s:
    #     print(i)
    res = json.dumps(s, ensure_ascii=False, indent=4)
    print(res)


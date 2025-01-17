import os
import json
from http.client import responses
import re
import logging

from config import LOG_DIR
# import requests
# from datetime import datetime, timedelta
#
# import pandas as pd
# from config import DATA_DIR, operations_path_xlsx
# from dotenv import load_dotenv
from src.utils import xlsx_reading, numcards_list, main_list


utils_log_path = os.path.join(LOG_DIR, "services.log")

logger = logging.getLogger("services")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(utils_log_path, mode='w+')
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s : %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def simple_search(main_list, pattern):
    """Функция реализует поиск по ключам Категория и Описание"""
    # pattern = input("Найти: ")
    res = []
    for i in main_list:
        if (type(i["Категория"]) == str) and (re.findall(pattern, i["Категория"], flags=re.IGNORECASE)) or (re.findall(pattern, i["Описание"], flags=re.IGNORECASE)):
            res.append(i)
    logger.info("Simple search list is forming")
    return json.dumps(res, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    print(simple_search(main_list, "Ozon"))

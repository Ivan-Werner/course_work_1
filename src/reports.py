import os
import json
from http.client import responses
import re
from typing import Optional
from unittest.mock import inplace

import requests
import calendar
from datetime import datetime, timedelta
import logging
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame
from config import LOG_DIR
from config import DATA_DIR, operations_path_xlsx
from dotenv import load_dotenv
from src.utils import xlsx_reading, numcards_list, main_list

transactions = pd.DataFrame(main_list)

utils_log_path = os.path.join(LOG_DIR, "reports.log")

logger = logging.getLogger("reports")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(utils_log_path, mode='w+')
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s : %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def csv_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.to_csv("report_category.csv", index=False)
    return wrapper



date_now = datetime.now().date()
date = date_now.strftime("%d.%m.%Y")

@csv_decorator
def spending_by_category(transactions: pd.DataFrame, category: str, date=date) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
    main_list = transactions.to_dict("records")
    source_category_list = []
    res = []
    for i in main_list:
        if i["Категория"] == category:
            source_category_list.append(i)
    logger.info("Source category list is forming")
    current_date = datetime.strptime(date, "%d.%m.%Y").date()
    days_in_month = calendar.monthrange(current_date.year, current_date.month)[1]
    left_date = current_date - timedelta(days=days_in_month) * 3
    for i in source_category_list:
        date_payment = datetime.strptime(i["Дата платежа"], "%d.%m.%Y").date()
        if left_date <= date_payment <= current_date:
            res.append(i)
    logger.info("Output result DataFrame")
    return pd.DataFrame(res)



if __name__ == '__main__':
    # for i in main_list:
    #     print(i)
    # print(date_now)
    # result = spending_by_category(transactions, "Цветы", "10.10.2021")
    # print(result)
    spending_by_category(transactions, "Цветы", "10.10.2021")


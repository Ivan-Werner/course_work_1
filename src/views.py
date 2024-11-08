import os
import json
from datetime import datetime, timedelta

import pandas as pd
from config import DATA_DIR, operations_path_xlsx


def xlsx_reading(operations_path_xlsx: str):
    try:
        py_file = pd.read_excel(operations_path_xlsx)
        py_dict = py_file.to_dict(orient='records')
        return py_dict
    except Exception:
        return []

def greetings(user_name: str):
    current_date = datetime.now()
    current_date += timedelta(hours=1)
    # print(current_date.hour)
    if current_date.hour > 4 and current_date.hour <= 12:
        print(f"{user_name}, доброе утро!")
    elif current_date.hour > 12 and current_date.hour <= 18:
        print(f"{user_name}, добрый день!")
    elif current_date.hour > 18 and current_date.hour <= 0:
        print(f"{user_name, }, добрый вечер!")
    else:
        print(f"{user_name}, доброй ночи!")



if __name__ == '__main__':
    # print(greetings("John"))
    # print(xlsx_reading(operations_path_xlsx))
    main_list = xlsx_reading(operations_path_xlsx)










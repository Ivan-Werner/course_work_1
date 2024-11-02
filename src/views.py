import os
import json
import pandas as pd
from config import DATA_DIR
operations_path_xlsx = os.path.join(DATA_DIR, "../data/operations.xlsx")

def xlsx_reading(operations_path_xlsx: str):
    try:
        py_file = pd.read_excel(operations_path_xlsx)
        py_dict = py_file.to_dict(orient='records')
        return py_dict
    except Exception:
        return []

if __name__ == '__main__':
    print(xlsx_reading(operations_path_xlsx)[0])






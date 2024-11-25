import os
import json
from http.client import responses

import requests
from datetime import datetime, timedelta

import pandas as pd
from config import DATA_DIR, operations_path_xlsx
from dotenv import load_dotenv
from views import xlsx_reading, numcards_list, main_list

print(xlsx_reading(operations_path_xlsx))
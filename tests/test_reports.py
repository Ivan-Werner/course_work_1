from operator import index

import pandas as pd
import pytest

from unittest import mock
import pandas as pd
from src.reports import csv_decorator

@csv_decorator
def test_function():
    """Возвращаем DataFrame с данными"""
    data = {'call_1': [1, 2], 'call_2': [3, 4]}
    df = pd.DataFrame(data)
    return df

@pytest.fixture
def mocker():
    with mock.patch('pandas.DataFrame.to_csv') as mock_to_csv:
        yield mock_to_csv


def test_csv_decorator(mocker):
    """СОздаем моку для проверки поведения"""
    mock_to_csv = mocker

    test_function()
    #Проверяем, что метод to_csv был вызван с правильными аргументами
    mock_to_csv.assert_called_once_with('report_category.csv', index=False)

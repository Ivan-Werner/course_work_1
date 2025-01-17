from src.utils import xlsx_reading, main_list, numcards_list, spent, cards_list, total_spent, currencies, \
    top_transactions, cashback, currency_price, stock_api
from tests.conftest import test_main_list, short_top_transactions, test_empty_file, test_currencies_list
from unittest.mock import patch
import pytest


def test_empty_xlsx_reading(test_empty_file):
    assert xlsx_reading(test_empty_file) == []


def test_numcards_list(test_main_list):
    assert numcards_list(test_main_list) == ['*7197', '*4556']


def test_spent(test_main_list, test_cards_list):
    assert spent(test_main_list, test_cards_list) == [240, -173760]


def test_cashback(test_total_spent):
    assert cashback(test_total_spent) == [23195.86, 23345.04, 17892.51]


def test_top_transactions(test_main_list, short_top_transactions):
    assert top_transactions(test_main_list) == short_top_transactions


@patch('')
def test_stock_api():




def test_currencies(test_main_list):
    assert currencies(test_main_list) == ['CNY', 'USD']




# @patch('requests.get')
# def test_currency_price(mock_get):
#     price_tested =
#     mock_get.return_value.status_code = 200





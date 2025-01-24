import pytest

from src.utils import xlsx_reading, numcards_list, spent, currencies, top_transactions, cashback,stock_api
from tests.conftest import test_main_list, short_top_transactions, test_empty_file
from unittest import mock


def _create_stock(amount):
    return {'stock': 'MSFT', 'price': amount}


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


MOCK_RESPONSE_DATA = {
    'data': [
        {
            'symbol': 'MSFT',
            'price': '150.00'
        },
        {
            'symbol': 'AAPL',
            'price': '200.00'
        },
        {
            'symbol': 'IBM',
            'price': '100.00'
        }
    ]
}


@pytest.fixture
def mocker():
    with mock.patch('requests.get') as mock_get:
        yield mock_get


@pytest.fixture(autouse=True)
def set_env_vars(monkeypatch):
    monkeypatch.setenv("API_KEY_stocks", "fake_token")


def test_stock_api(mocker):
    mock_response = mocker.Mock()
    mock_response.return_value.json.return_value = MOCK_RESPONSE_DATA
    mock_get = mocker
    result = stock_api()

    assert mock_get.called
    assert result == []


def test_currencies(test_main_list):
    assert currencies(test_main_list) == ['CNY', 'USD']

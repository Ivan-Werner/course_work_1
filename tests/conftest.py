import pytest


@pytest.fixture
def test_empty_file():
    return []

@pytest.fixture
def test_main_list():
    short_main_list = [
        {
        'Дата операции': '31.12.2021 16:44:00',
             'Дата платежа': '31.12.2021',
             'Номер карты': '*7197',
             'Статус': 'OK',
             'Сумма операции': -160.89,
             'Валюта операции': 'RUB',
             'Сумма платежа': -160.89,
             'Валюта платежа': 'RUB',
             'Кэшбэк': None,
             'Категория': 'Супермаркеты',
             'MCC': 5411.0, 'Описание': 'Колхоз',
             'Бонусы (включая кэшбэк)': 3,
             'Округление на инвесткопилку': 0,
             'Сумма операции с округлением': 160.89
        },
        {
            'Дата операции': '31.12.2021 16:42:04',
            'Дата платежа': '31.12.2021',
            'Номер карты': '*7197',
            'Статус': 'OK',
            'Сумма операции': -64.0,
            'Валюта операции': 'RUB',
            'Сумма платежа': -64.0,
            'Валюта платежа': 'RUB',
            'Кэшбэк': None,
            'Категория': 'Супермаркеты',
            'MCC': 5411.0,
            'Описание': 'Колхоз',
            'Бонусы (включая кэшбэк)': 1,
            'Округление на инвесткопилку': 0,
            'Сумма операции с округлением': 64.0
        },
        {'Дата операции': '30.12.2021 17:50:17',
         'Дата платежа': '30.12.2021',
         'Номер карты': '*4556',
         'Статус': 'OK',
         'Сумма операции': 174000.0,
         'Валюта операции': 'RUB',
         'Сумма платежа': 174000.0,
         'Валюта платежа': 'RUB',
         'Кэшбэк': None,
         'Категория': 'Пополнения',
         'MCC': None,
         'Описание': 'Пополнение через Газпромбанк',
         'Бонусы (включая кэшбэк)': 0,
         'Округление на инвесткопилку': 0,
         'Сумма операции с округлением': 174000.0
        },
        {'Дата операции': '30.08.2021 20:35:38',
         'Дата платежа': '30.08.2021',
         'Номер карты': '*7197',
         'Статус': 'OK',
         'Сумма операции': -15.0,
         'Валюта операции': 'USD',
         'Сумма платежа': -1129.5,
         'Валюта платежа': 'RUB',
         'Кэшбэк': None,
         'Категория': 'НКО',
         'MCC': 8398.0,
         'Описание': 'Association For Computing',
         'Бонусы (включая кэшбэк)': 22,
         'Округление на инвесткопилку': 0,
         'Сумма операции с округлением': 1129.5
        },
        {'Дата операции': '01.10.2019 14:01:02',
         'Дата платежа': '01.10.2019',
         'Номер карты': None,
         'Статус': 'OK',
         'Сумма операции': -13.67,
         'Валюта операции': 'CNY',
         'Сумма платежа': -13.67,
         'Валюта платежа': 'CNY',
         'Кэшбэк': None,
         'Категория': 'Переводы',
         'MCC': None,
         'Описание': 'Перевод между счетами',
         'Бонусы (включая кэшбэк)': 0,
         'Округление на инвесткопилку': 0,
         'Сумма операции с округлением': 13.67
         }

    ]

    return short_main_list


@pytest.fixture
def test_cards_list():
    return ['*7197', '*4556']

@pytest.fixture
def test_total_spent():
    return [2319586, 2334504, 1789251]

@pytest.fixture
def short_top_transactions():
    return [{'amount': 174000.0,
             'category': 'Пополнения',
             'date': '30.12.2021',
             'description': 'Пополнение через Газпромбанк'},
            {'amount': -13.67,
             'category': 'Переводы',
             'date': '01.10.2019',
             'description': 'Перевод между счетами'},
            {'amount': -64.0,
             'category': 'Супермаркеты',
             'date': '31.12.2021',
             'description': 'Колхоз'},
            {'amount': -160.89,
             'category': 'Супермаркеты',
             'date': '31.12.2021',
             'description': 'Колхоз'},
            {'amount': -1129.5,
             'category': 'НКО',
             'date': '30.08.2021',
             'description': 'Association For Computing'}]

@pytest.fixture
def test_pattern():
    return "НКО"

@pytest.fixture
def test_currencies_list():
    return ['CNY', 'USD']

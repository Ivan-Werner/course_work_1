
from src.reports import spending_by_category, transactions_df, date_today
from src.services import simple_search
from src.utils import (cards_list, cashback, currencies, currency_price,
                       main_list, numcards_list, spent, stock_api,
                       top_transactions, total_spent)
from src.views import greetings, res_output


def transactions_running():
    """Функция выводит информацию с главной страницы"""
    print("Выводим статистику по банковским транзакциям:\n")
    web = res_output(greetings(), numcards_list(main_list), spent(main_list, cards_list), cashback(total_spent),
                     top_transactions(main_list), currency_price(currencies(main_list)), stock_api())
    return web


def service_running():
    """Функция выводит резульат поиска по транзакциям"""
    pattern = input("Введите параметр поиска по банковским транзакциям:\n")
    service = simple_search(main_list, pattern)
    print(service)


# def report_running():
#     """Функция формирует отчет в формате CSV по тратам за 3 месяца"""
#     try:
#         category = input("Введите название категории:\n")
#         date = input("Введите дату в формате '10.10.2021' либо нажмите Enter, для выбора текущей даты:\n")
#         return spending_by_category(transactions_df, category, date=date)
#     except ValueError:
#         print("Неверный формат даты")

def report_running():
    """Функция формирует отчет в формате CSV по тратам за 3 месяца"""
    category = input("Введите название категории:\n")
    date = input("Введите дату в формате '10.10.2021' либо нажмите Enter, для выбора текущей даты:\n")
    try:
        if len(date) == 0:
            return spending_by_category(transactions_df, category)
        else:
            return spending_by_category(transactions_df, category, date=date)
    except ValueError:
        print("Неверный формат даты")


if __name__ == '__main__':
    print(transactions_running())
    service_running()
    report_running()

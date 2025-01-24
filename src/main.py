
from src.views import res_output, greetings
from src.utils import (main_list, numcards_list, spent, cards_list, cashback, total_spent, top_transactions,
                       currency_price, currencies, stock_api)
from src.services import simple_search
from src.reports import spending_by_category, transactions

def transactions_running():
    print("Выводим статистику по банковским транзакциям:\n")
    web = res_output(greetings(), numcards_list(main_list), spent(main_list, cards_list), cashback(total_spent),
                     top_transactions(main_list), currency_price(currencies(main_list)), stock_api())
    return web

def service_running():
    pattern = input("Введите параметр поиска по банковским транзакциям:\n")
    service = simple_search(main_list, pattern)
    print(service)


def report_running():
    try:
        category = input("Введите название категории:\n")
        date = input("Введите дату в формате '10.10.2021' либо нажмите Enter, для выбора текущей даты:\n")
        return spending_by_category(transactions, category, date=date)
    except ValueError:
        print("Неверный формат даты")

if __name__ == '__main__':
    # print(transactions_running())
    # service_running()
    report_running()


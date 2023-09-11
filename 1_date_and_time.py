"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta


def print_days():
    now = datetime.now()
    yesterday = timedelta(days=1)
    thirtн_days_ago = timedelta(days=30)
    
    print(datetime.date(now))
    print(datetime.date(now-yesterday))
    print(datetime.date(now-thirtн_days_ago))


def str_2_datetime(date_string):
    date = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))

"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_TIME, ('RU','UTF8'))

def print_days():
    dt_now = datetime.now()
    delta_day = timedelta(days=1)
    delta_month = timedelta(days=30)
    dt_yesterday = (dt_now -delta_day).strftime('%A %d %B %Y')
    dt_month_ago = (dt_now -delta_month).strftime('%A %d %B %Y')
    dt_now = dt_now.strftime('%A %d %B %Y')
    print (f'Вчера было: {dt_yesterday}, сегодня {dt_now}, а месяц назад {dt_month_ago}')

def str_2_datetime(date_string):
    date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date_dt
if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))

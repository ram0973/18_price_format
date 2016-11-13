# -*- coding: utf-8 -*-
import argparse

import sys

import decimal
from decimal import Decimal


def format_price(price: str) -> str:
    """
    :param price: из базы данных приходит строка вида 3245.000000
    :return: cтрока вида 3 245 или None
    """
    try:
        return ' '.join('{:,}'.format(int(Decimal(price))).split(','))
    except (ValueError, decimal.InvalidOperation):
        return None


def enable_win_unicode_console():
    """
    Включаем правильное отображение unicode в консоли под MS Windows
    """
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


def main():
    enable_win_unicode_console()

    parser = argparse.ArgumentParser()
    parser.add_argument('--string', '--s',
                        help='Введите строку вида 3245.000000',
                        required=True)

    string = parser.parse_args().string
    print('Результат: ', format_price(string))


if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
import argparse
from decimal import Decimal, InvalidOperation


def format_price(price: str) -> str:
    """
    Форматирование цены с десятичными разрядами в виде пробелов и
    отбрасыванием дробной части
    :param price: строка вида 3245.000000
    :return: cтрока вида 3 245 или None
    """
    try:
        return ' '.join('{:,}'.format(int(Decimal(price))).split(','))
    except InvalidOperation:
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--string', '--s', required=True,
                        help='Введите строку вида 3245.000000')
    string = parser.parse_args().string
    print('Результат работы функции format_price(): ', format_price(string))


if __name__ == '__main__':
    main()
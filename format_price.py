# -*- coding: utf-8 -*-
import argparse
from decimal import Decimal, InvalidOperation


def format_price(price):
    try:
        return ' '.join('{:,}'.format(int(Decimal(price))).split(','))
    except InvalidOperation:
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--string', '--s', required=True,
                        help='Enter string like 3245.000000')
    string = parser.parse_args().string
    print('Result of format_price(): ', format_price(string))

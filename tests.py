import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_price_is_numeric(self):
        price = format_price('12O.3')
        self.assertEqual(price, None)

    def test_price_correctly_cleared_from_spaces_or_tnr(self):
        price = format_price(' \t\n\r  \t   234.454555   \n  \r   \t\n\r ')
        self.assertEqual(price, '234')

    def test_price_have_space_delimiters(self):
        price = format_price('123456789.123456 ')
        self.assertEqual(price, '123 456 789')

    def test_price_truncates_fractional_part(self):
        price = format_price('123.123456 ')
        self.assertEqual(price, '123')

    def test_price_keeps_minus_sign(self):
        price = format_price('-123456.123456 ')
        self.assertEqual(price, '-123 456')

    def test_price_ignoring_plus_sign(self):
        price = format_price('+123456.123456 ')
        self.assertEqual(price, '123 456')

    def test_price_can_be_negative_and_have_no_integer_part(self):
        price = format_price('-.123456 ')
        self.assertEqual(price, '0')

    def test_price_can_be_positive_and_have_no_integer_part(self):
        price = format_price('.123456 ')
        self.assertEqual(price, '0')

    def test_price_can_have_no_fractional_part(self):
        price = format_price('-123456789.')
        self.assertEqual(price, '-123 456 789')

    def test_price_can_have_no_dot(self):
        price = format_price('-123456789')
        self.assertEqual(price, '-123 456 789')

    def test_price_is_not_rounding(self):
        price = format_price('1.999999999999999999999999999999999999999999999')
        self.assertEqual(price, '1')

    def test_price_can_be_huge(self):
        price = format_price('999999999999999999999999999999999')
        self.assertEqual(price, '999 999 999 999 999 999 999 999 999 999 999')

if __name__ == '__main__':
    unittest.main()


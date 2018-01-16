import unittest
from currency.symbol import get_currency_from_symbol

from configparser import ConfigParser


class TestGetCurrencyFromSymbol(unittest.TestCase):

    def test_get_currency_from_symbol(self):
        config = ConfigParser()
        config.set("s", "s1", "S1")

        input1 = "s1"
        self.assertEqual(get_currency_from_symbol(input1, config), "S1")

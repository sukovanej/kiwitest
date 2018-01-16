import unittest
from currency.symbol import get_currency_from_symbol

from configparser import ConfigParser


class TestGetCurrencyFromSymbol(unittest.TestCase):

    def test_get_currency_from_symbol(self):
        config = ConfigParser()
        config.add_section('symbols')
        config["symbols"]  = {
            "s1": "S1",
            "s2": "S2"
        }

        input1 = "s1"
        input2 = "s2"
        input3 = "old"

        self.assertEqual(get_currency_from_symbol(input1, config), "S1")
        self.assertEqual(get_currency_from_symbol(input2, config), "S2")
        self.assertEqual(get_currency_from_symbol(input3, config), "old")

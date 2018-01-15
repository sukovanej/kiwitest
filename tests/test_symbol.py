import unittest
from currency.symbol import get_currency_from_symbol
from configparser import ConfigParser

class TestGetCurrencyFromSymbol(unittest.TestCase):
    def GetCurrencyFromSymbol(self):
        config = ConfigParser()
        config.set("s", "s1", "S1")

        input1 = "s1"
        self.assertEqual(get_currency_from_symbol(input1, config), "S1")

if __name__ == "__main__":
    unittest.main()

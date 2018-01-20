from configparser import ConfigParser
from currency.symbol import get_currency_from_symbol

class Converter:

    def __init__(self, config):
        self.precision = int(config.get("data", "precision"))
        self.datafile = config.get("data", "file")
        self.currency_data = self.load_data(self.datafile)

    def load_data(self, filename):
        currency_data = dict()

        with open(filename, "r") as file_obj:
            for line in file_obj:
                if not line.strip():
                    continue

                data = line.strip().split("=")
                if len(data) != 2:
                    raise ValueError("Data format error ({})".format(data))

                currency_data[data[0]] = float(data[1])

        return currency_data

    def convert_from_to(self, from_currency, to_currency):
        return round(self.currency_data[from_currency] / self.currency_data[to_currency], self.precision)

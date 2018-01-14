from configparser import ConfigParser

class Converter:

    def __init__(self, config):
        self.datafile = self.get_data_file(config)
        self.currency_data = self.load_data(self.datafile)

    def get_data_file(self, config):
        return config.get("data", "file")

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
        return self.currency_data[from_currency] / self.currency_data[to_currency]

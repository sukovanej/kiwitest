class Converter(object):

    def __init__(self, config):
        self.precision = config.getint("data", "precision")
        self.currency_data = self.load_data("/etc/currency_converter/currency_data.txt")

    def load_data(self, filename):
        currency_data = dict()

        with open(filename) as file_obj:
            for line_raw in file_obj:
                line = line_raw.strip()
                if not line:
                    continue

                data = line.split("=")
                if len(data) != 2:
                    raise ValueError("Data format error ({})".format(data))

                currency_data[data[0]] = float(data[1])

        return currency_data

    def convert_from_to(self, from_currency, to_currency):
        return round(self.currency_data[from_currency] /
                     self.currency_data[to_currency], self.precision)

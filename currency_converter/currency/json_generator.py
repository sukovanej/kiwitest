import json


class JsonGenerator(object):

    def __init__(self, converter):
        self.converter = converter

    def create_json(self, currency_from, currency_to, amount):
        result_currency_to = dict()
        result_currency_from = {"amount": amount, "currency": currency_from}

        if currency_to == "ALL":
            result_currency_to = self.get_all_currencies(
                currency_from, amount)
        else:
            result_currency_to = {
                currency_to: self.converter.convert_from_to(
                    currency_from, currency_to) * float(amount)
            }

        return json.dumps({
            "input": result_currency_from,
            "output": result_currency_to
        })

    def get_all_currencies(self, currency_from, amount):
        result = dict()

        for key in self.converter.pool.scan_iter("*"):
            currency_to = key.decode('utf-8')

            if currency_to == currency_from:
                continue

            result[currency_to] = self.converter.convert_from_to(
                currency_from, currency_to) * float(amount)

        return result

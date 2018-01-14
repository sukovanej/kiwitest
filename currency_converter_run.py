from flask import Flask, request
from configparser import ConfigParser
from currency.converter import Converter
from currency.json_generator import JsonGenerator
import json

app = Flask(__name__)

@app.route('/currency_converter')
def currency_converter():
    try:
        amount = request.args.get("amount", default=1)
        input_currency = request.args.get("input_currency")
        output_currency = request.args.get("output_currency", default="ALL")

        if input_currency == None:
            raise ValueError("input_currency must be specified")

        return json_generator.create_json(input_currency, output_currency, amount)
    except ValueError as e:
        return json.dumps({"error": str(e)})

def main():
    global json_generator
    config = ConfigParser()
    config.read("config.ini")

    converter = Converter(config)
    json_generator = JsonGenerator(converter)

    app.run()

if __name__ == "__main__":
    main()

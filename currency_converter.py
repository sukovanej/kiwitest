from argparse import ArgumentParser
from configparser import ConfigParser
from src.converter import Converter
from src.json_generator import JsonGenerator

def setup_defaults(config):
    return {
        "amount": config.get("default", "amount"),
        "input_currency": config.get("default", "input_currency"),
        "output_currency": config.get("default", "output_currency")
    }

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('--amount', help='An amount of money')
    parser.add_argument('--input_currency', help='Currency input')
    parser.add_argument('--output_currency', help='Currency output')

    return {key: value for key, value in vars(parser.parse_args()).items() if value != None}

def main():
    config = ConfigParser()
    config.read("config.ini")

    defaults = setup_defaults(config)
    arguments = parse_arguments()

    input_values = { **defaults, **arguments } # use defaults and override with arguments

    converter = Converter(config)
    json_generator = JsonGenerator(converter)

    print(json_generator.create_json(
        input_values["input_currency"],
        input_values["output_currency"],
        input_values["amount"]
    ))

if __name__ == "__main__":
    main()

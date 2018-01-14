#!/usr/local/bin/python3
import argparse
import configparser

def setup_defaults():
    config = configparser.ConfigParser()
    config.read("config.ini")

    return {
        "amount": config.get("default", "amount"),
        "input_currency": config.get("default", "input_currency"),
        "output_currency": config.get("default", "output_currency")
    }

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--amount', help='An amount of money')
    parser.add_argument('--input_currency', help='Currency input')
    parser.add_argument('--output_currency', help='Currency output')

    return {key: value for key, value in vars(parser.parse_args()).items() if value != None}

def main():
    defaults = setup_defaults()
    arguments = parse_arguments()

    input_values = { **defaults, **arguments }
    print(input_values)

if __name__ == "__main__":
    main()

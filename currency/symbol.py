def get_currency_from_symbol(symbol, config):
    new_symbol = config["symbols"].get(symbol, symbol)

    if new_symbol == None:
        return symbol
    else:
        return new_symbol

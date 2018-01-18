def get_currency_from_symbol(symbol, config):
    return config["symbols"].get(symbol, symbol)

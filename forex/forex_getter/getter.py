from forex_python.converter import CurrencyRates


def get_rates(pool) :
    c = CurrencyRates()
    rates = c.get_rates("USD")

    pipe = pool.pipeline()

    for (currency, value) in rates.items():
        pipe.set(currency, 1 / value)

    pipe.set('USD', 1)
    pipe.execute()

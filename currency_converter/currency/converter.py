import redis


class Converter(object):

    def __init__(self, config):
        self.pool = redis.Redis(host='redis', port=6379, db=0)
        self.precision = config.getint('data', 'precision')

    def convert_from_to(self, from_currency, to_currency):
        return round(self.pool.get(from_currency) / self.pool.get(to_currency),
                     self.precision)

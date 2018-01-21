import redis


class Converter(object):

    def __init__(self, config):
        self.pool = redis.Redis(host='redis', port=6379, db=0)
        self.precision = config.getint('data', 'precision')

    def convert_from_to(self, from_currency, to_currency):
        return round(float(self.pool.get(from_currency).decode('utf-8')) /
            float(self.pool.get(to_currency).decode('utf-8')), self.precision)

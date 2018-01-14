from configparser import ConfigParser
import unittest
from src.converter import Converter

class TestConverter(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestConverter, self).__init__(*args, **kwargs)

        config = ConfigParser()
        config.read("config.ini")

        self.converter = Converter(config)
        self.converter.currency_data = self.__test_data()

    @staticmethod
    def __test_data():
        return {
            "A": 1,
            "B": 2,
            "C": 1.5,
            "D": 0.5,
        }

    def test_covert_from_to(self):
        a_to_b = self.converter.convert_from_to("A", "B");
        a_to_c = self.converter.convert_from_to("A", "C");
        a_to_d = self.converter.convert_from_to("A", "D");
        b_to_a = self.converter.convert_from_to("B", "A");
        b_to_c = self.converter.convert_from_to("B", "C");
        b_to_d = self.converter.convert_from_to("B", "D");
        c_to_a = self.converter.convert_from_to("C", "A");
        c_to_b = self.converter.convert_from_to("C", "B");
        c_to_d = self.converter.convert_from_to("C", "D");

        self.assertEqual(a_to_b, 1/2)
        self.assertEqual(a_to_c, 1/1.5)
        self.assertEqual(a_to_d, 1/0.5)
        self.assertEqual(b_to_a, 2/1)
        self.assertEqual(b_to_c, 2/1.5)
        self.assertEqual(b_to_d, 2/0.5)
        self.assertEqual(c_to_a, 1.5/1)
        self.assertEqual(c_to_b, 1.5/2)
        self.assertEqual(c_to_d, 1.5/0.5)

if __name__ == "__main__":
    unittest.main()

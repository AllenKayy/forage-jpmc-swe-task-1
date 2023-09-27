import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote),
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                              (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote),
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                              (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    """ ------------ Add more unit tests ------------ """

    def test_getDataPoint_zeroAskPrice(self):
        # Test when the ask price is zero.
        quote = {'top_ask': {'price': 0, 'size': 0}, 'timestamp': '2019-02-11 22:06:30.572453',
                 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
        self.assertEqual(getDataPoint(quote),
                         (quote['stock'], quote['top_bid']['price'], 0, quote['top_bid']['price'] / 2))

    def test_getDataPoint_negativeBidPrice(self):
        # Test when the bid price is negative.
        quote = {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                 'top_bid': {'price': -5.0, 'size': 10}, 'id': '0.109974697771', 'stock': 'XYZ'}
        self.assertEqual(getDataPoint(quote),
                         (quote['stock'], -5.0, quote['top_ask']['price'], (quote['top_ask']['price'] - 5.0) / 2))

    def test_getRatio_bothNonZero(self):
        # Test when both price_a and price_b are non-zero.
        result = getRatio(10, 5)
        self.assertEqual(result, 2.0)

    def test_getRatio_priceAZero(self):
        # Test when price_a is zero and price_b is non-zero.
        result = getRatio(0, 5)
        self.assertEqual(result, 0.0)

    def test_getRatio_priceBZero(self):
        # Test when price_b is zero and price_a is non-zero.
        result = getRatio(10, 0)
        self.assertIsNone(result)

    def test_getRatio_bothZero(self):
        # Test when both price_a and price_b are zero.
        result = getRatio(0, 0)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()

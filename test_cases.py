from price_feed import *
import unittest

class TestPriceFeed(unittest.TestCase):
    def test_get_latest_ETH_price(self):
        latest_ETH_price=get_latest_ETH_price()
        self.assertEqual(str(type(latest_ETH_price)),"<class 'float'>")

    def test_record_ETH_prices(self):
        self.assertEqual(record_ETH_prices(),True)

    def test_calculate_mean_of_ETH_price(self):
        self.assertEqual(str(type(calculate_mean_of_ETH_price())),"<class 'float'>")

    def test_update_record(self):
        for i in range(20):
            self.assertEqual(str(type(update_record(i))),"<class 'bool'>")

    def test_delete_record(self):
        for i in range(20):
            self.assertEqual(str(type(delete_record(i))),"<class 'bool'>")

        
if __name__=='__main__':
    unittest.main()

import unittest
import example

class TestMyFunc(unittest.TestCase):

    def test_ma_kota(self):
        self.assertEqual(example.ma_kota("Ala"), "Ala ma kota.")

if __name__ == '__main__':
    unittest.main()

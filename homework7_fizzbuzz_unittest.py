
import unittest
import fizzbuzz

def test_fizzbuzz(self):
    for i in range(100):
        result = fizzbuzz.fizzbuzz(i)
        self.assertEqual(result, i)


if __name__ == "__main__":
    unittest.main()
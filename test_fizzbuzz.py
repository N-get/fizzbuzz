
import unittest
import fizzbuzz
class fizz(unittest.TestCase):
    def test_fizzbuzz(self):
        for i in range(100):
            result = fizzbuzz.fizzbuzz(i)
            self.assertEqual(result, i)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(fizz('test_fizzbuzz'))

    unittest.TextTestRunner().run(suite)
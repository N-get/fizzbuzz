
import unittest
import fizzbuzz
class fizz(unittest.TestCase):
    def test_fizzbuzz(self):
        for i in range(100):
            if (i == 0):
                i = 1
            result = fizzbuzz.fizzbuzz(i)
            if(i % 3 == 0):
                self.assertEqual(result, "fizz")
            else:
                self.assertEqual(result, i)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(fizz('test_fizzbuzz'))

    unittest.TextTestRunner().run(suite)
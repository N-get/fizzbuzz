
import unittest
import fizzbuzz
class fizz(unittest.TestCase):
    def test_fizzbuzz(self):
        for i in range(1, 101):
            result = fizzbuzz.fizzbuzz(i)
            if(i % 3 == 0 and i % 5 == 0):
                self.assertEqual(result, "FizzBuzz")
            elif(i % 3 == 0):
                self.assertEqual(result, "Fizz")
            elif(i % 5 == 0):
                self.assertEqual(result, "Buzz")
            else:
                self.assertEqual(result, i)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(fizz('test_fizzbuzz'))

    unittest.TextTestRunner().run(suite)
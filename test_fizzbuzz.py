
import unittest
import fizzbuzz
class fizz(unittest.TestCase):
    def test_fizzbuzz(self):
        for i in range(101):
            if (i == 0):
                i = 1
            result = fizzbuzz.fizzbuzz(i)
            if(i % 3 == 0 and i % 5 == 0):
                self.assertEqual(result, "fizzbuzz")
            elif(i % 3 == 0):
                self.assertEqual(result, "fizz")
            elif(i % 5 == 0):
                self.assertEqual(result, "buzz")
            else:
                self.assertEqual(result, i)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(fizz('test_fizzbuzz'))

    unittest.TextTestRunner().run(suite)
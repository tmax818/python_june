import unittest
import functions_basic_ii as file


print(type(file.countdown))

class TestFunctions(unittest.TestCase):

    def test_countdown_exists(self):
        self.assertIsInstance(file.countdown, function)

    def test_countdown(self):
        self.assertEqual(file.countdown(5), [5,4,3,2,1,0])

    

if __name__ == '__main__':
    unittest.main()
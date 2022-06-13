import unittest
import functions_basic_ii as file


print(type(file.countdown))

class TestFunctions(unittest.TestCase):

    def test_countdown(self):
        self.assertEqual(file.countdown(5), [5,4,3,2,1,0])

    def test_print_and_return(self):
        pass


    def test_first_plus_length(self):
        pass

    def test_values_greater_than_second(self):
        pass

    def test_length_and_value(self):
        pass

    

if __name__ == '__main__':
    unittest.main()
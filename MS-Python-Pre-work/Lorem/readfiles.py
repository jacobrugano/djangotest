import unittest
import readfiles

class TestReadFiles(unittest.TestCase):
    """
    Class to test the  functions on the  readfiles module

    Args:
        unittest.TestCase: Class from the unittest module to create unit tests
    """
    
text_file = "test.txt"
def read_file(text_file):
    """
    Function that reads a text file and returns the data from the text file
        """
    with open(text_file,"r") as handle:
        data = handle.read()
        return data


if __name__ == "__main__":
    unittest.main()
import unittest
from capitalize_letter import capitalize_first_letter

class TestCapitalizeFirstLetter(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = capitalize_first_letter(text)
        self.assertEqual(result, 'Python', 'Should capitalize the first letter of the string')
    
    def test_multiple_words(self):
        result = capitalize_first_letter('osaretin igbinobaro')
        self.assertEqual(result, 'Osaretin Igbinobaro', 'Should capitalize the first letter of every word')

    

# run this test file if the script is run directly (doesn't run if imported)
if __name__ == '__main__':
     unittest.main()

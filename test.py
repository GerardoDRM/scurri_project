import unittest
from app import get_multiples, UK_PostCodes

'''
 This class tests the multiples of five and three
'''
class TestMultiples(unittest.TestCase):

    def test_default_serie(self):
        num_multiples = len(get_multiples(1, 16))
        self.assertEqual(num_multiples, 7)

    def test_negative_numbers(self):
        num_multiples = len(get_multiples(-1,-16))
        self.assertEqual(num_multiples, 7)

    def test_correct_values(self):
        num_multiples = get_multiples(9, 16)
        # Validate in a range from 9 to 16 the numbers printed as string
        values = ["Three", "Five", "Three", "ThreeFive"]
        self.assertEqual(num_multiples, values)


'''
 This class tests all functions on UK postcodes problems
'''
class TestUKPostCodes(unittest.TestCase):

    def test_validate_codes(self):
        postcode_scanner = UK_PostCodes()
        correct_examples = ['TN15 6NG',
                            'BH9 3PT',
                            'SW15 5LH',
                            'PL8 1HH',
                            'bt23 6rs']

        bad_examples = ['TN15_6NG',
                        'BH9;;2355PT',
                        '1SW15++5LH',
                        'PL8 1HH1',
                        'CH13d',
                        '']

        # Validate all correct postcode examples
        for e in correct_examples:
            self.assertTrue(postcode_scanner.validate_code(e))

        # Validate all bad postcodes, some of this postcodes can be accepted with formatting
        for e in bad_examples:
            self.assertFalse(postcode_scanner.validate_code(e))

    def test_formatting(self):
        postcode_scanner = UK_PostCodes()
        # Return a string with the correct uk format
        self.assertEqual(postcode_scanner.validate_format("TN15'=___6'nG"), "TN15 6NG")

    def test_is_ukpostcode(self):
        postcode_scanner = UK_PostCodes()
        # Use validation and formatting to determinate if it is a correct UK postcode
        self.assertTrue(postcode_scanner.is_an_ukpostcode("TN15'=___6'nG"))
        self.assertFalse(postcode_scanner.is_an_ukpostcode("1SW15++5LH"))

if __name__ == '__main__':
    unittest.main()

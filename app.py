import re
import math

class UK_PostCodes:
    '''
        This class supports validating and formatting post codes for UK
        based on https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
    '''

    # Validation pattern taken from https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
    # provided by the UK goverment
    VALIDATION_PATTERN = '^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$'

    '''
        Function which normalizes the postcode format
        @param postcode - str
        @return str
    '''
    def validate_format(self, postcode):
        # Extract just alphanumeric values and normalize the value to uppercase
        code = re.sub(r'[\W_]+', '', postcode).upper()
        # Adding format to Inward code (3 characters at the end and a space
        # between inward and outward)
        return "%s %s" % (code[:-3], code[-3:])

    '''
        Function which validates the postcode with the regular expression pattern
        @param postcode - str
        @return bool
    '''
    def validate_code(self, postcode):
        # Check if it is a match between the poscode and the regex pattern
        if re.match(self.VALIDATION_PATTERN, postcode):
            return True
        return False

    '''
        Function which supports validating and formatting
        @param postcode - str
        @return bool
    '''
    def is_an_ukpostcode(self, postcode):
        code = self.validate_format(postcode)
        return self.validate_code(code)


'''
    Function which checks if a number sequence has multiples of three and five
    @param offset int
    @param limit int
    @return array of multiples just for Testing case
'''
def get_multiples(offset=1, limit=100):
    multiples = []
    for i in range(int(math.fabs(offset)), int(math.fabs(limit))):
        if i % 3 == 0 and i % 5 == 0:
            print("ThreeFive")
            multiples.append("ThreeFive")
        elif i % 3 == 0:
            print("Three")
            multiples.append("Three")
        elif i % 5 == 0:
            print("Five")
            multiples.append("Five")
        else:
            print(i)


    return multiples

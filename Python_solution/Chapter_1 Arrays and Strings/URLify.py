# URLify
# Created by JKChang
# 20/02/2018, 12:16
# Tag:
# Description: Write a method to replace all spaces in a string with '%20'. You may assume that the string has
#              sufficient space at the end to hold the additional characters, and that you are given the 'true' length
#              of of the string.
# Example: Input "Mr John Smith    " 13
#          Output "Mr%20John%20Smith"

import unittest


def urlify(string, length):
    """" function to replace all spaces in a string with '%20' and remove trailing space"""
    #   res =string[:length].replace(' ', '%20')
    res = ['%20' if c == ' ' else c for c in string[:length]]
    print(''.join(res))
    return list(''.join(res))



class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much do about nothing      '), 21,
         list('much%20do%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

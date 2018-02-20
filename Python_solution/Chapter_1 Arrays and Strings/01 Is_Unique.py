# 01 Is_Unique
# Created by JKChang
# 20/02/2018, 11:25
# Tag:
# Description: implement a algorithm to determine if a string has all unique characters. What is you cannot use
#              additional data structure?

# O(N)
import unittest


def unique(string):
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]

    for char in string:
        val = ord(char)  # Return the Unicode code point for a one-character string.
        if char_set[val]:
            return False
        char_set[val] = True
    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()'), ('  ')]

    def test_unique(self):
        # True
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # False
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()

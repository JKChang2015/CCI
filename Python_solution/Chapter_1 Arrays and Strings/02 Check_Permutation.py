# 02 Check_Permutation
# Created by JKChang
# 20/02/2018, 12:01
# Tag:
# Description: Given two strings, write a method to decide if on e is a permutation of the other

# Hint:A permutation, also called an “arrangement number” or “order,” is a rearrangement of the elements of an ordered
#      list S into a one-to-one correspondence with S itself.

# O(N)

import unittest
from collections import Counter


def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    counter = Counter()
    for char in str1:
        counter[char] += 1

    for char in str2:
        if counter[char] == 0:
            return False
        counter[char] -= 1

    return True


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # True
        for test_string in self.dataT:
            result = check_permutation(*test_string)
            self.assertTrue(result)

        for test_string in self.dataF:
            result = check_permutation(*test_string)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()

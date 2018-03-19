#!/usr/bin/env python 

import unittest
from random import Random

def num_gen():
    """
    Return random number between 1 and 100, inclusive
    """
    return random.randint(1, 100) 

class num_gen_Test(unittest.TestCase):

    def setUp(self):
        global random
        random = Random(123)

    def test_num_gen(self):
        self.assertEqual(num_gen(), 7)

if __name__ == '__main__':
    unittest.main()

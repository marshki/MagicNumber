#!/usr/bin/env python

"""Test suite.
"""

from random import Random

import unittest

random = Random()

def num_gen():
    """Generate random integer between 1 and 100, inclusive.
    """
    return random.randint(1, 100)

class NumGenTest(unittest.TestCase):
    """Test class.
    """

    def setUp(self):
        """Set seed value.
        """
        global random
        random = Random(123)

    def test_num_gen_01(self):
        """Valid return value.
        """
        self.assertEqual(num_gen(), 7)

    def test_num_gen_02(self):
        """Invalid return value.
        """
        self.assertNotEqual(num_gen(), 49)

if __name__ == '__main__':
    unittest.main()

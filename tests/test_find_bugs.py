import unittest
import numpy as np


def magic_function(a, b):
    """ magic function that divides a by b.

    :param float a: numerator
    :param float b: denumerator of division
    :return: a/b
    """

    return a / b

class TestMagicFunction(unittest.TestCase):
    def test_function(self):
        """Test for magic_function. It tests 5 cases."""
        for a, b, answer in ((1, 1, 1), (2, 1, 2), (1, 3, 0.3333333), (-2, 1, -2), (2, 0, np.inf)):
            self.assertEqual(magic_function(a, b), answer,
                             msg=f"division of {a} by {b} does not equal {answer}.")


if __name__=='__main__':
    unittest.main()




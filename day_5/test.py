import unittest

from day_5.day_5 import react_polymer


class Day5Test(unittest.TestCase):

    def test_single_reaction(self):
        polymer = 'bB'
        result = react_polymer(polymer)
        expected = ''

        self.assertEqual(result, expected)

    def test_reacts_to_nothing(self):
        polymer = 'abBA'
        result = react_polymer(polymer)
        expected = ''

        self.assertEqual(result, expected)

    def test_simple_nothing_reacts(self):
        polymer = 'aabAAB'
        result = react_polymer(polymer)
        expected = 'aabAAB'

        self.assertEqual(result, expected)

    def test_example(self):
        polymer = 'dabAcCaCBAcCcaDA'
        result = react_polymer(polymer)

        expected = 'dabCBAcaDA'

        self.assertEqual(result, expected)

    def test_symmetric(self):
        polymer = 'abcdefgGFEDCBA'
        result = react_polymer(polymer)

        expected = ''

        self.assertEqual(result, expected)

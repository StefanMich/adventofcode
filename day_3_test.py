import unittest

from day_3 import Claim, empty_fabric, overlap_claims


class Day3TEst(unittest.TestCase):

    def test_add_claim(self):
        claims = self.example_data()

        fabric = empty_fabric()

        for claim in claims:
            claim.add_claim(fabric)

        for vertical in range(9):
            for horizontal in range(9):
                inch = fabric[vertical][horizontal]
                if vertical == 4 and horizontal == 4:
                    self.assertEqual(inch, 2)
                elif ((vertical <= 4 and horizontal <= 4)
                      or (vertical >= 4 and horizontal >= 4)):
                    self.assertEqual(inch, 1)
                else:
                    self.assertEqual(inch, 0)

    def test_overlap(self):
        claims = self.example_data()

        fabric = empty_fabric()

        for claim in claims:
            claim.add_claim(fabric)

        self.assertEqual(overlap_claims(fabric), 1)

    def test_line_to_claim(self):
        claim = Claim('#1 @ 2,3: 4x5')
        self.assertEqual(claim.id, 1)
        self.assertEqual(claim.left_margin, 2)
        self.assertEqual(claim.top_margin, 3)
        self.assertEqual(claim.width, 4)
        self.assertEqual(claim.height, 5)

    def test_aoc_example(self):
        fabric = empty_fabric()
        for line in ["#1 @ 1,3: 4x4",
                      "#2 @ 3,1: 4x4",
                      "#3 @ 5,5: 2x2"]:
            Claim(line).add_claim(fabric)

        self.assertEqual(overlap_claims(fabric), 4)

    def example_data(self):
        return [Claim('#1 @ 0,0: 5x5'),
                Claim('#2 @ 4,4: 5x5')]


if __name__ == '__main__':
    unittest.main()

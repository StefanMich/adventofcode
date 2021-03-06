import re
from collections import defaultdict


def empty_fabric():
    return defaultdict(lambda: defaultdict(lambda: list()))


def print_fabric(fabric):
    widest = 0
    for vertical in fabric.values():
        l = len(vertical)
        if l > widest:
            widest = l

    for vertical in range(len(fabric)):
        for horizontal in range(widest):
            print(len(fabric[vertical][horizontal]), end='')
        print()


def overlap_claims(fabric):
    overlaps = 0
    for vertical in fabric.values():
        for horizontal in vertical.values():
            if len(horizontal) > 1:
                overlaps += 1
    return overlaps


class Claim():
    def __init__(self, line):
        regex = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
        parsed = regex.search(line)
        self.id, self.left_margin, self.top_margin, self.width, self.height = map(int, parsed.groups())

    def add_claim(self, fabric):
        for vertical in range(self.left_margin, self.left_margin + self.width):
            for horizontal in range(self.top_margin, self.top_margin + self.height):
                fabric[vertical][horizontal].append(self.id)

    def alone_claim(self, fabric):
        for vertical in range(self.left_margin, self.left_margin + self.width):
            for horizontal in range(self.top_margin, self.top_margin + self.height):
                inch = fabric[vertical][horizontal]
                if len(inch) != 1:
                    return False
        return True


if __name__ == '__main__':
    fabric = empty_fabric()

    with open('day_3_input') as f:
        input_strings = f.read()

    for line in input_strings.split('\n'):
        if not line:
            continue

        claim = Claim(line)
        claim.add_claim(fabric)

    for line in input_strings.split('\n'):
        if not line:
            continue

        claim = Claim(line)
        if claim.alone_claim(fabric):
            print(claim.id)

    print(overlap_claims(fabric))
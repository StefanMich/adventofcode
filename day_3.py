import re
from collections import defaultdict


def empty_fabric():
    return defaultdict(lambda: defaultdict(lambda: 0))

def overlap_claims(fabric):
    overlaps = 0
    for vertical in fabric.values():
        for horizontal in vertical.values():
            if horizontal > 1:
                overlaps += 1
    return overlaps

class Claim():
    def __init__(self, line):
        regex = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
        parsed = regex.search(line)
        # 1322 @ 149,715: 16x14

        id, rest = line.split('@')
        self.id = int(id[1:])
        margins, size = rest.split(':')

        left_margin, top_margin = margins.split(',')
        self.left_margin = int(left_margin)
        self.top_margin = int(top_margin)

        width, height = size.split('x')
        self.width = int(width)
        self.height = int(height)

    def add_claim(self, fabric):
        for vertical in range(self.left_margin, self.left_margin + self.width):
            for horizontal in range(self.top_margin, self.top_margin + self.width):
                fabric[vertical][horizontal] += 1


fabric = empty_fabric()

with open('day_3_input') as f:
    input_strings = f.read()

for line in input_strings.split('\n'):
    if not line:
        continue

    claim = Claim(line)
    claim.add_claim(fabric)

print(overlap_claims(fabric))
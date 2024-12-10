import itertools

from src.index import Index
from src.reader import Reader


class Cell:
    def __init__(self, element: str):
        self.antinode = False
        if element == ".":
            self.antenna = None
        else:
            self.antenna = element

    def __str__(self):
        if self.antinode:
            return "#"
        elif self.antenna:
            return self.antenna
        else:
            return "."

    def __repr__(self):
        return str(self)

    def is_antenna(self) -> bool:
        return self.antenna is not None


example = False

## Part 1

with Reader(8, example) as reader:
    field = reader.get_field("", Cell)


# print(*field, sep="\n")


antennas = dict()
for i, line in enumerate(field):
    for j, cell in enumerate(line):
        if cell.is_antenna():
            if cell.antenna not in antennas:
                antennas[cell.antenna] = list()
            antennas[cell.antenna].append(Index(i, j))


antinodes = set()
for antenna, indices in antennas.items():
    pairs = itertools.combinations(indices, 2)
    for a1, a2 in pairs:
        diff = a2 - a1

        anti = a2 + diff
        if anti.is_in(field):
            antinodes.add(anti)

        anti = a1 - diff
        if anti.is_in(field):
            antinodes.add(anti)

total = len(antinodes)
print("Part 1:", total)


## Part 2

antinodes = set()
for antenna, indices in antennas.items():
    pairs = itertools.combinations(indices, 2)
    for a1, a2 in pairs:
        # The antena is an antinode
        antinodes.add(a1)
        antinodes.add(a2)

        diff = a2 - a1

        a2 += diff
        while a2.is_in(field):
            antinodes.add(a2)
            a2 = a2 + diff

        a1 -= diff
        while a1.is_in(field):
            antinodes.add(a1)
            a1 -= diff


total = len(antinodes)
print("Part 2:", total)

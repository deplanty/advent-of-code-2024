import copy

from src import Debug, Reader


debug = Debug()
example = False


class Towel:
    def __init__(self):
        self.colors: str = str()
        self.debug = Debug(False)

    def __str__(self) -> str:
        return self.colors

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return hash(self.colors)

    def add(self, pattern: str, design:str) -> bool:
        """Try to add the pattern to match the design"""
        n_current = len(self.colors)
        n_size = len(pattern)

        self.debug(n_current, n_size, design[n_current : n_size], pattern, end=" ")
        if design[n_current : n_current + n_size] == pattern:
            self.colors += pattern
            self.debug("OK")
            return True
        else:
            self.debug("X")
            return False

    def match(self, design:str) -> bool:
        return self.colors == design


## Part 1

# debug.disable()

with Reader(19, example) as reader:
    patterns = reader.get_line(", ")
    reader.raw_line()
    designs = [line for line in reader.iter_lines()]

# Store the first color of each pattern
# starts: dict[str, list[str]] = dict()
# for pattern in patterns:
#     x = pattern[0]
#     if x not in starts:
#         starts[x] = list()
#     starts[x].append(pattern)

# Try to find if all the designs can be created
found = 0
for i, design in enumerate(designs, 1):
    debug(f"Design {i}/{len(designs)}: design")
    # Init the towels
    towels: set[Towel] = set()
    for pattern in patterns:
        towel = Towel()
        added = towel.add(pattern, design)
        if added:
            towels.add(towel)
    # Find the patterns for the towels
    seen: set[str] = set()
    search = True
    count = 10_000
    while towels and search and count > 0:
        # debug("Towels:", len(towels))
        next_towels: set[Towel] = set()
        for towel in towels:
            for pattern in patterns:
                new_towel = copy.deepcopy(towel)
                added = new_towel.add(pattern, design)
                if new_towel.colors in seen:
                    continue
                if new_towel.match(design):
                    search = False
                    found += 1
                    debug("FIND:", new_towel)
                    break
                if added:
                    next_towels.add(new_towel)
                    seen.add(new_towel.colors)

            # Do not look more towels if the design has been found
            if not search:
                break

        towels = next_towels
        count -= 1
    debug()

print("Part 1:", found)

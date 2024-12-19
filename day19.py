import copy

from src import Debug, Reader


debug = Debug()
example = False


class Towel:
    def __init__(self):
        self.patterns: list[str] = list()
        self.debug = Debug(False)

    def __str__(self) -> str:
        return self.colors

    def __repr__(self) -> str:
        return " ".join(self.patterns)

    def __hash__(self) -> int:
        return hash(self.colors)

    def __len__(self) -> int:
        return len(self.colors)

    @property
    def colors(self) -> str:
        return "".join(self.patterns)

    def can_add(self, pattern: str, design: str) -> bool:
        """Check if the pattern can be add to make the design"""

        n_current = len(self.colors)
        n_size = len(pattern)
        self.debug(n_current, n_size, design[n_current:n_size], pattern, end=" ")
        return design[n_current : n_current + n_size] == pattern

    def add(self, pattern: str):
        """Add the pattern to the towel"""

        self.patterns.append(pattern)

    def match(self, design: str) -> bool:
        """Return if the towel match the design"""

        return self.colors == design


## Part 1

with Reader(19, example) as reader:
    patterns = reader.get_line(", ")
    reader.raw_line()
    designs = [line for line in reader.iter_lines()]

# Try to find if all the designs can be created
found: set[str] = set()
not_found: set[str] = set()
for i, design in enumerate(designs, 1):
    debug(f"P1 Design {i}/{len(designs)}: design")
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
                    found.add(design)
                    debug("FIND:", design)
                    break
                if added:
                    next_towels.add(new_towel)
                    seen.add(new_towel.colors)

            # Do not look more towels if the design has been found
            if not search:
                break

        towels = next_towels
        count -= 1

    if search:
        not_found.add(design)
        debug("NOT FIND:", design)
    debug()

# debug("Found", found, sep="\n")

print("Part 1:", len(found))

## Part 2

# Remove the designs that can't be made
# for design in not_found:
#     designs.remove(design)

# Try to find if all the designs and arrangements
found = 0
for i, design in enumerate(designs, 1):
    debug(f"P2 Design {i}/{len(designs)}: {design}")
    # Init the towels
    towels: set[Towel] = set()
    for pattern in patterns:
        towel = Towel()
        if towel.can_add(pattern, design):
            towel.add(pattern)
            towels.add(towel)
    # Find the patterns for the towels
    unmakable: set[str] = set()  # Last part of a design unmakable
    count = 10_000
    while towels and count > 0:
        # debug("Towels:", len(towels))
        next_towels: set[Towel] = set()
        for towel in towels:
            makable = False
            for pattern in patterns:
                new_towel = copy.deepcopy(towel)
                can_add = new_towel.can_add(pattern, design)
                # Skip if the pattern cannot be added to the towel
                if not can_add:
                    continue
                # Add the pattern and check if the towel is valid or match the full design
                new_towel.add(pattern)
                makable = True
                if len(new_towel) > len(design):
                    continue
                elif new_towel.match(design):
                    found += 1
                    debug("FIND:", design)
                    break

                next_towels.add(new_towel)
            if not makable:
                unmakable.add(towel)
        towels = next_towels
        count -= 1

    debug()

print("Part 2:", found)

from src import Debug, Reader, Index


class Region:
    def __init__(self, symbol: str, *index: Index):
        self.symbol = symbol
        self.positions: set[Index] = set()
        for ind in index:
            self.positions.update(ind)

    def __str__(self) -> str:
        return f"Region {self.symbol}"

    def area(self) -> int:
        return len(self.positions)

    def is_next(self, index: Index) -> bool:
        for neighbour in index.NESW:
            if neighbour in self.positions:
                return True
        return False

    def can_fuse(self, region: "Region") -> bool:
        if self.symbol != region.symbol:
            return False

        for index in region.positions:
            if self.is_next(index):
                return True

        return False

    def fuse(self, region: "Region"):
        self.positions.update(region.positions)

    def count_edges(self) -> int:
        count = 0
        for index in self.positions:
            edges = 4
            for neighbour in index.NESW:
                if neighbour in self.positions:
                    edges -= 1
            count += edges
        return count

    def count_sides(self) -> int:
        corners = 0

        for index in self.positions:
            tests = [
                (index.N, index.E, index.NE),
                (index.E, index.S, index.SE),
                (index.S, index.W, index.SW),
                (index.W, index.N, index.NW),
            ]
            for side1, side2, corner in tests:
                s1 = side1 in self.positions
                s2 = side2 in self.positions
                c = corner in self.positions

                if not s1 and not s2:
                    debug("Corner extern:", index)
                    corners += 1
                if s1 and s2 and not c:
                    debug("Corner intern:", index)
                    corners += 1
        return corners


debug = Debug()
example = False


with Reader(12, example) as reader:
    table = reader.get_table("", str)

debug("Table")
debug(*table, sep="\n")
debug()


visited: set[Index] = set()
regions: list[Region] = list()
for i, line in enumerate(table):
    for j, symbol in enumerate(line):
        # For each position in the table
        index = Index(i, j)
        if index in visited:
            continue

        # From this position, find all the connected elements with the same symbol
        connected: set[Index] = {index}  # The list of the connected symbols
        visited_current: set[Index] = (
            set()
        )  # The visited positions for the connected symbols
        current: set[Index] = {index}  # The current symbols seen
        while current:
            next_current: set[Index] = set()
            for ind in current:
                for neighbours in ind.NESW:
                    if neighbours in visited_current:
                        continue
                    visited_current.add(neighbours)
                    if neighbours.is_in(table) and neighbours.get(table) == symbol:
                        connected.add(neighbours)
                        visited.add(neighbours)
                        next_current.add(neighbours)
            current = next_current

        if connected:
            region = Region(symbol, connected)
            regions.append(region)

## Part 1

debug.disable()
total = 0
for region in regions:
    price = region.count_edges() * region.area()
    debug(
        f"Region {region.symbol} | area {region.area()} | edges {region.count_edges()} | price {price}"
    )
    total += price
print("Part 1:", total)

## Part 2

debug()
total = 0
for region in regions:
    debug(f"Region {region.symbol}")
    sides = region.count_sides()
    area = region.area()
    price = sides * area
    debug(f"area {area} * sides {sides} = price {price}")
    total += price
print("Part 2:", total)

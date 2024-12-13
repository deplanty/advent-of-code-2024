from src import Reader, Debug, Index


class Path(list):
    def __init__(self, start: Index):
        super().__init__()
        self.append(start)

    @property
    def first(self) -> Index:
        return self[0]

    @property
    def last(self) -> Index:
        return self[-1]


debug = Debug(True)

example = True

with Reader(10, example) as reader:
    table = reader.get_table("", int)


starts = set()
for i, line in enumerate(table):
    for j, val in enumerate(line):
        if val == 0:
            starts.add(Index(i, j))

debug(*table, sep="\n")
debug(starts)
debug()

all_pathes: list[Path] = [Path(index) for index in starts]

for start in starts:
    # For all the possible starts, check all the passages
    ends: dict[Index, set] = {index: set() for index in starts}
    visited: set[Index] = starts.copy()
    currents: set[Index] = starts.copy()
    pathes: list[Path]
    while currents:
        print(currents)
        next_positions = set()
        # Look for all the current positions
        for index in currents:
            value = index.get(table)
            if value == 9:
                ends.add(index)
                continue

            # Look for all the neighbours
            for position in index.NESW:
                if not position.is_in(table):
                    continue
                if position in visited:
                    continue
                if position.get(table) == value + 1:
                    next_positions.add(position)

        visited.update(next_positions)
        currents = next_positions

debug(ends)
total = len(ends)
print("Part 1:", total)

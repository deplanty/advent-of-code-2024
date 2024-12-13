import copy

from src import Reader, Debug, Index


debug = Debug(False)
example = False

## Part 1

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

pathes: list[list[Index]] = [[index] for index in starts]
pathes_ok: list[list[Index]] = list()

count = 1_000
while pathes and count > 0:
    new_pathes: list[list[Index]] = list()

    for path in pathes:
        debug(f"Path {path}", end=" | ")
        # Check if the last value is the end of a path
        value = path[-1].get(table)
        if value == 9:
            debug("end of road")
            pathes_ok.append(path)
            continue

        # Look for all the neighbours
        for position in path[-1].NESW:
            if not position.is_in(table):
                debug(f"{position} ✗", end=" | ")
                continue
            if position.get(table) == value + 1:
                tmp = copy.deepcopy(path)
                tmp.append(position)
                new_pathes.append(tmp)
                debug(f"{position} ✓", end=" | ")
            else:
                debug(f"{position} ✗", end=" | ")
        debug()

    pathes = new_pathes
    count -= 1

    debug()

# Get the reachable peaks
trails = dict()
for path in pathes_ok:
    head = path[0]
    if head not in trails:
        trails[head] = set()
    trails[head].add(path[-1])

total = 0
for head, peaks in trails.items():
    debug(head, len(peaks))
    total += len(peaks)
print("Part 1:", total)

## Part 2

total = len(pathes_ok)
print("Part 2:", total)

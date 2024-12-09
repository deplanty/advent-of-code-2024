import copy
import itertools

from src.reader import Reader
from src.index import Index


example = False

## Part 1

with Reader(6, example) as reader:
    field = reader.get_table("")

    current = Index(0, 0)
    for i, line in enumerate(field):
        if "^" in line:
            j = line.index("^")
            current = Index(i, j)  # autoformater add some shit()


directions = itertools.cycle(
    [Index.delta_N, Index.delta_E, Index.delta_S, Index.delta_W]
)
direction = next(directions)
visited = {current}
count = 10_000
while current.is_in(field) and count > 0:
    target = current + direction
    if not target.is_in(field):
        break
    if target.get(field) == "#":
        direction = next(directions)
    else:
        current = target
        visited.add(current)
    count -= 1

total = len(visited)
print("Part 1:", total)

## Part 2


def next_direction(index: Index) -> Index:
    if index == Index.delta_N:
        return Index.delta_E
    elif index == Index.delta_E:
        return Index.delta_S
    elif index == Index.delta_S:
        return Index.delta_W
    elif index == Index.delta_W:
        return Index.delta_N


with Reader(6, example) as reader:
    field = reader.get_table("")

    start = Index(0, 0)
    for i, line in enumerate(field):
        if "^" in line:
            j = line.index("^")
            start = Index(i, j)


total = 0
for i in range(len(field)):
    for j in range(len(field[0])):
        test = Index(i, j)

        # Not the starting position
        if test == start:
            continue

        # Add a block
        field_tmp = copy.deepcopy(field)
        test.set(field_tmp, "#")

        current = start
        direction = Index.delta_N

        count = 10_000
        while count > 0:
            target = current + direction
            if not target.is_in(field_tmp):
                break
            if target.get(field_tmp) == "#":
                direction = next_direction(direction)
            else:
                current = target
            count -= 1
        else:
            print(i, j, "ok")
            total += 1

print("Part 2:", total)

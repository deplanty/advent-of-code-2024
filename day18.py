import copy

from src import Debug, Reader, Index
from src.show import Show


debug = Debug()
example = False


with Reader(18, example) as reader:
    positions: list[Index] = list()
    for x, y in reader.iter_split(",", int):
        positions.append(Index(y, x))


# Const
WALL = "#"
EMPTY = "."

size: int = {
    True: 7,   # Example
    False: 71, # Input
}.get(example)

start = Index(0, 0)
end = Index(size - 1, size - 1)

## Part 1

firsts: int = {
    True: 12,    # Example
    False: 1204, # Input
}.get(example)

# Create the field
field: list[list[str]] = [[EMPTY for _ in range(size)] for _ in range(size)]
for i in range(firsts):
    index = positions[i]
    index.set(field, WALL)

# Find the shortest path
paths: list[list[Index]] = [[start]]
visited: set[Index] = set()
path_found = None
search = True
count = 10_000
while search and count > 0:
    next_paths: list[list[Index]] = list()
    count -= 1

    for path in paths:
        for target in path[-1].get_neighbours_4():
            # Target should be in the field
            if not target.is_in(field):
                continue
            # Target should not go to an already visited position
            elif target in visited:
                continue
            # Target should not be a corrupted path
            elif target.get(field) == WALL:
                continue
            # Target can be an empty space
            elif target.get(field) == EMPTY:
                new_path = copy.deepcopy(path)
                new_path.append(target)
                visited.add(target)
                if target == end:
                    search = False
                    path_found = new_path
                else:
                    next_paths.append(new_path)

    paths = next_paths



total = len(path_found) - 1
print("Part 1:", total)

# show = Show(4)
# show.show_table(field, {"#": "black"})
# show.show_coords(path_found, "red")
# show.mainloop()

## Part 2

def find_a_path(field: list[list[str]], start: Index, end: Index) -> list[Index]:
    """
    Find a path from the start position to the end position.
    Return the found path.
    """

    paths: list[list[Index]] = [[start]]
    visited: set[Index] = set()
    search = True
    count = 10_000
    while search and count > 0:
        next_paths: list[list[Index]] = list()
        count -= 1

        for path in paths:
            for target in path[-1].get_neighbours_4():
                # Target should be in the field
                if not target.is_in(field):
                    continue
                # Target should not go to an already visited position
                elif target in visited:
                    continue
                # Target should not be a corrupted path
                elif target.get(field) == WALL:
                    continue
                # Target can be an empty space
                elif target.get(field) == EMPTY:
                    new_path = copy.deepcopy(path)
                    new_path.append(target)
                    visited.add(target)
                    if target == end:
                        return new_path
                    else:
                        next_paths.append(new_path)

        paths = next_paths
    return []


# Create the field
field: list[list[str]] = [[EMPTY for _ in range(size)] for _ in range(size)]

# The first elements can't bloc the field
i = 1
for index in positions[: size - 1]:
    index.set(field, "#")
    i += 1

path = find_a_path(field, start, end)
# Find the position that will block the path
for index in positions[size - 1 :]:
    debug(f"{i} / {len(positions)}")
    index.set(field, "#")
    # Check if the current path is still ok
    another = False
    for index in path:
        if index.get(field) == "#":
            another = True
            break

    if another:
        path = find_a_path(field, start, end)

    # show = Show(16)
    # show.show_table(field, {"#": "black"})
    # show.show_coords(path_tmp, "red")
    # show.mainloop()

    i += 1
    if not path:
        break

print(f"Part 2: {index.j},{index.i}")

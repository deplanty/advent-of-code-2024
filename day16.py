import copy

from src import Debug, Reader, Index, Chrono
from src.show import Show


class Path(list):
    def __init__(self, init: list[Index] = list(), init_cost: int = 0, init_direction: Index = Index.delta_E):
        super().__init__()
        self.extend(init)
        self.cost = init_cost
        self.direction = init_direction


def move_and_cost(direction: Index) -> tuple[tuple[Index, int]]:
    if direction == Index.delta_N:
        return (Index.delta_W, 1001), (Index.delta_N, 1), (Index.delta_E, 1001)
    elif direction == Index.delta_E:
        return (Index.delta_N, 1001), (Index.delta_E, 1), (Index.delta_S, 1001)
    elif direction == Index.delta_S:
        return (Index.delta_E, 1001), (Index.delta_S, 1), (Index.delta_W, 1001)
    elif direction == Index.delta_W:
        return (Index.delta_S, 1001), (Index.delta_W, 1), (Index.delta_N, 1001)


debug = Debug()
example = True

WALL = "#"
EMPTY = "."
START = "S"
END = "E"

## Part 1

with Reader(16, example) as reader:
    field = reader.get_field("")

# Find start and end point
start: Index
end: Index
for i, line in enumerate(field):
    for j, char in enumerate(line):
        if char == START:
            start = Index(i, j)
        elif char == END:
            end = Index(i, j)

# debug.show_field(field)
# debug()
# debug(f"Start: {start}")
# debug(f"End: {end}")
# debug()


chrono = Chrono()

paths: list[Path] = [Path([start])]
visited: set[Index] = set()
search = True
count = 100_000
while search and count > 0:
    # Get path with the least cost
    path = min(paths, key=lambda p: p.cost)
    paths.remove(path)
    for delta, cost in move_and_cost(path.direction):
        target: Index = path[-1] + delta
        if target.get(field) == WALL:
            continue
        elif target in path:
            continue
        elif target in visited:
            continue
        elif target.get(field) == EMPTY:
            new_path = copy.deepcopy(path)
            new_path.append(target)
            new_path.direction = delta
            new_path.cost += cost
            paths.append(new_path)
            visited.add(target)
        elif target.get(field) == END:
            search = False
            path_find = copy.deepcopy(path)
            path_find.append(target)
            path_find.direction = delta
            path_find.cost += cost
            break

    count -= 1

chrono.stop()

total = path_find.cost
print("Part 1:", total)
debug(chrono.text)

## Part 2


# Change field to store the cost in the field
field_cost: list[list] = list()
for line in field:
    new_line: list = list()
    for char in line:
        if char in (EMPTY, START, END):
            char = float("inf")
        new_line.append(char)
    field_cost.append(new_line)

chrono.start()

paths: list[Path] = [Path([start])]
paths_to_end: list[Path] = list()
least_cost = path_find.cost
count = 100_000
while paths and count > 0:
    # Get path with the least cost
    path = min(paths, key=lambda p: p.cost)

    show = Show(20)
    show.show_table(field, {"#": "black", "S": "green", "E": "red"})
    show.show_coords(path, "blue")
    show.mainloop()

    paths.remove(path)
    # For all the possible directions from here
    for delta, cost in move_and_cost(path.direction):
        target: Index = path[-1] + delta
        # If the target is a wall, do nothing
        if target.get(field_cost) == WALL:
            continue
        # If the target position is an int = empty space
        elif isinstance(target.get(field_cost), (int, float)):
            # Update the path
            new_path = copy.deepcopy(path)
            new_path.append(target)
            new_path.direction = delta
            new_path.cost += cost

            # Go to next target if the cost is greater to the one present
            debug(f"Test cost: {new_path.cost} vs. {target.get(field_cost)}")
            if new_path.cost > target.get(field_cost):
                continue
            # If the target reach the end
            if target == end:
                paths_to_end.append(path_find)
            else:
                paths.append(new_path)

            target.set(field_cost, new_path.cost)

    count -= 1

chrono.stop()

# debug("Paths found:", len(paths_to_end))

# show = Show(20)
# show.show_table(field, {"#": "black", "S": "green", "E": "red"})
# for path in paths_to_end:
#     show.show_coords(path, "blue")
# show.mainloop()


all_cells = set()
for path in paths_to_end:
    all_cells.update(path)
total = len(all_cells)
print("Part 2:", total)
debug(chrono.text)

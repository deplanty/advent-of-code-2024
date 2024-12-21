from src import Debug, Reader, Index

from src.show import Show


debug = Debug()
example = True

WALL = "#"
EMPTY = "."
START = "S"
END = "E"


with Reader(20, example) as reader:
    field = reader.get_field("")

for i, line in enumerate(field):
    for j, char in enumerate(line):
        if char == START:
            start = Index(i, j)
        elif char == END:
            end = Index(i, j)


def find_track(field: list[list[str]], start: Index, end: Index):
    """Get the position order of each position in the track"""

    path: list[Index] = [start]
    while path[-1] != end:
        for neig in path[-1].get_neighbours_4():
            if (neig not in path) and (
                neig.get(field) == EMPTY or neig.get(field) == END
            ):
                path.append(neig)
                break
    return path


def get_cheat_coords(index: Index, path: list[Index], field: list[list[str]], duration: int) -> list[Index]:
    next_indices = list()
    border: list[Index] = [index]
    i = path.index(index)
    tmp_path = set(path[: i])
    seen = {start}
    for _ in range(duration):
        next_border: list[Index] = list()
        for bd in border:
            for neig in bd.get_neighbours_4():
                if neig in seen:
                    continue
                if neig in next_indices:
                    continue
                if neig in tmp_path:
                    continue

                seen.add(neig)
                next_border.append(neig)
                if neig.is_in(field) and neig.get(field) != WALL:
                    next_indices.append(neig)
        border = next_border

    return next_indices


# List all the coordinates of the track
debug("Path: ...", end="\r", flush=True)
path = find_track(field, start, end)
debug("Path: found!", flush=True)

## Part 1
duration = 2

## Part 2
duration = 20


path_indices = {index: i for i, index in enumerate(path)}

# Find all the cheats
thresh = {
    True: 50,
    False: 100,
}.get(example)
total = 0
hist = dict()
for i, index in enumerate(path):
    debug(f"{i + 1} / {len(path)}", end="\r", flush=True)
    for cheat in get_cheat_coords(index, path, field, duration):
        position = path_indices[cheat]
        saved = position - i - 2
        if saved >= thresh:
            if saved not in hist:
                hist[saved] = 0
            hist[saved] += 1
            total += 1

        if saved >= 80:
            show = Show(32)
            show.show_table(field, {WALL: "black", EMPTY: "lightgrey", START: "red", END: "red"})
            rg = get_cheat_coords(index, path, field, duration)
            show.show_coords(rg, "teal")
            show.show_coords([index, cheat], "lime")
            show.mainloop()

print("Part 1 or 2:", total)
debug(hist)

# Part 2 with example: 259
# Found 561
#
# Part 2 with input:
# X too low
# X too high

scale = {
    True: 32,
    False: 5,
}.get(example)
show = Show(scale)
show.show_table(field, {WALL: "black", EMPTY: "lightgrey", START: "red", END: "red"})
rg = get_cheat_coords(start, path, field, duration)
show.show_coords(rg, "teal")
show.mainloop()

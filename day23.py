import copy

from src import Debug, Reader


debug = Debug()
example = True


def get_groups(start: str, connections: dict[str, list[str]], max_size: int = 3):
    groups: set[tuple[str]] = set()
    currents = [[start]]
    count = 10_000
    while currents and count > 0:
        new_currents = list()
        for group in currents:
            last = group[-1]
            for computer in connections[last]:
                # If loop, stop
                if computer == start:
                    if len(group) != 2:
                        groups.add(tuple(group))
                    continue

                new_group = copy.deepcopy(group)
                new_group.append(computer)
                # A group can't be bigger than max_size
                if len(new_group) > max_size:
                    continue
                else:
                    new_currents.append(new_group)

        currents = new_currents
        count -= 1
    return groups


with Reader(23, example) as reader:
    connections: dict[str, list[str]] = dict()
    for a, b in reader.iter_split("-", str):
        if a not in connections:
            connections[a] = list()
        connections[a].append(b)
        if b not in connections:
            connections[b] = list()
        connections[b].append(a)

n_computers = len(connections)

# for computer, group in connections.items():
#     debug(computer, len(group))

## Part 1

debug.disable()

# Find all unique groups
all_groups: set[tuple[str]] = set()
for computer in connections:
    groups = get_groups(computer, connections)
    for group in groups:
        all_groups.add(tuple(sorted(group)))

debug(f"Groups of 3 computers: {len(all_groups)}")
debug(*all_groups, sep="\n")

# Find the computers where an ID starts with a t
total = 0
for group in all_groups:
    for computer in group:
        if computer.startswith("t"):
            total += 1
            break
print("Part 1:", total)

## Part 2

debug.enable()

with Reader(23, example) as reader:
    connections: dict[str, list[str]] = dict()
    for a, b in reader.iter_split("-", str):
        if a not in connections:
            connections[a] = list()
        connections[a].append(b)
        if b not in connections:
            connections[b] = list()
        connections[b].append(a)

# Find all unique groups
all_groups: set[tuple[str]] = set()
for i, computer in enumerate(connections, 1):
    debug(f"Computer {i}/{n_computers}: {computer}")
    groups = get_groups(computer, connections, 13)
    for group in groups:
        all_groups.add(tuple(sorted(group)))

debug(f"Groups of 13 computers: {len(all_groups)}")
debug(*all_groups, sep="\n")

print("Part 2:", total)

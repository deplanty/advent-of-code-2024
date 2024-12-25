from src import Debug, Reader


debug = Debug()
example = False

# Constants

EMPTY = "."
FULL = "#"


def read_schematics(raw: str) -> tuple[str, list[int]]:
    """
    Return the type of the schematic and its heights.
    """

    raw = raw.rstrip().split()

    # Get is the schematic is a key or a lock
    if all(x == FULL for x in raw[0]):
        type = "lock"
    elif all(x == FULL for x in raw[-1]):
        type = "key"
    else:
        raise ValueError("Raw schematic is neither a key nor a lock.")

    # Get the heights of the schematic
    heights: list[int] = list()
    for j in range(len(raw[0])):
        count = 0
        for i in range(len(raw)):
            if raw[i][j] == FULL:
                count += 1
        heights.append(count - 1)

    return type, heights


def can_fit(lock: list[int], key: list[int], height: int = 5) -> bool:
    if len(lock) != len(key):
        raise ValueError("Lock and key are not the same size.")

    for i in range(len(lock)):
        if lock[i] + key[i] > height:
            debug(f"Lock {lock} and key {key} overlap")
            return False

    debug(f"Lock {lock} and key {key} fit")
    return True


with Reader(25, example) as reader:
    raw = reader.read()
    schematics = raw.split("\n\n")
    locks = list()
    keys = list()
    for schematic in schematics:
        tp, heights = read_schematics(schematic)
        if tp == "lock":
            locks.append(heights)
        elif tp == "key":
            keys.append(heights)


## Part 1

total = 0
for lock in locks:
    for key in keys:
        if can_fit(lock, key):
            total += 1

print("Part 1:", total)

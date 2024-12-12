from src.reader import Reader


def calc_checksum(line: list[int]) -> int:
    total = 0
    for i, val in enumerate(line):
        if val is None:
            continue
        total += i * val

    return total


example = False

## Part 1

with Reader(9, example) as reader:
    line = reader.one_line()
    memory = [int(x) for x in line]


storage = list()
for i, val in enumerate(memory):
    if i % 2 == 0:
        storage.extend([i // 2] * val)
    else:
        storage.extend([None] * val)


i = 0
j = len(storage) - 1
while i < j:
    if storage[i] is None:
        storage[i] = storage[j]
        storage[j] = None
        j -= 1
        while storage[j] is None:
            j -= 1
    i += 1


total = calc_checksum(storage)
print("Part 1:", total)

## Part 2

sizes = dict()
storage = list()
for i, val in enumerate(memory):
    if i % 2 == 0:
        iid = i // 2
        storage.extend([iid] * val)
        sizes[iid] = val
    else:
        storage.extend([None] * val)
iid_order = list(reversed(sizes.keys()))

positions = dict()
for iid in sizes:
    positions[iid] = storage.index(iid)


# print(sizes)
# print(iid_order)
# print(storage)
# print()


for iid in iid_order:
    # The file we want to find some free space
    size = sizes[iid]
    tail = positions[iid]

    # print(f"Current is {iid} with size {size}")

    # Find first free space
    head = 0
    while head < tail:
        while storage[head] is not None:
            head += 1
        # print(f"    Head index {head} -> find free space")

        if head > tail:
            break

        # Find size of free space
        free = 0
        while head + free < len(storage) and storage[head + free] is None:
            free += 1
        # print(f"    Head index {head} -> find free space = size {free}")

        # Check if current file can fit
        if size <= free:
            # print(f"    Current {iid} fits in Head index {head} -> use {size}/{free} space")
            for i in range(size):
                storage[head + i] = iid
                storage[tail + i] = None
            break
        else:
            # print(f"    Current {iid} does not fit in Head index {head} -> use {size}/{free} space")
            head += min(size, free)

    # print(storage)
    # print()


total = calc_checksum(storage)
print("Part 2:", total)

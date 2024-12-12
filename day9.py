from src.reader import Reader


def calc_checksum(line: str) -> int:
    total = 0
    for i, val in enumerate(line):
        if val is None:
            break
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

from src.reader import Reader


def calc_checksum(line: list[int]) -> int:
    total = 0
    for i, val in enumerate(line):
        if val is None:
            break
        total += i * val

    return total


example = True

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


class MemorySlot:
    def __init__(self, size: int, iid: int = None):
        self.size = size
        self.iid = iid

    def __str__(self):
        return f"{self.iid}x{self.size}"

    def __repr__(self):
        return str(self)

    def checksum(self) -> int:
        if self.iid is None:
            return 0

        cs = 0
        for i in range(self.size):
            cs += i * self.iid
        return cs

    def is_file(self) -> bool:
        return self.iid is not None

    def is_empty(self) -> bool:
        return self.iid is None

    def can_fit(self, slot: "MemorySlot") -> bool:
        return self.size >= slot.size

    def clear(self):
        self.iid = None


def calc_checksum(line: list[MemorySlot]) -> int:
    total = 0
    i = 0
    for slot in line:
        if slot.is_empty():
            break
        for _ in range(slot.size):
            total += i * val
            i += 1

    return total


storage = list()
for i, size in enumerate(memory):
    if i % 2 == 0:
        iid = i // 2
    else:
        iid = None
    storage.append(MemorySlot(size, iid))


for j in range(len(storage), -1, -1):
    for i in range(j):
        if storage[i].is_file():
            continue

        if storage[i].can_fit(storage[j]):
            size_i = storage[i].size
            size_j = storage[j].size
            storage[i] = storage.pop(j)
            storage.insert(i + 1, MemorySlot(size_i - size_j, None))


line = list()
for slot in storage:
    if slot.is_empty():
        iid = "."
    else:
        iid = str(slot.iid)
    for _ in range(slot.size):
        line.append(iid)

print("".join(line))

total = calc_checksum(storage)
print("Part 2:", total)

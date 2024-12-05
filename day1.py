from src.reader import Reader

## Part 1

left = list()
right = list()
with Reader(1) as reader:
    left = list()
    right = list()
    for l, r in reader.iter_split("   ", int, int):
        left.append(l)
        right.append(r)

left = sorted(left)
right = sorted(right)

total =  0
for l, r in zip(left, right):
    total += abs(l - r)

print("Part 1:", total)

## Part 2

left = list()
right = list()
with Reader(1) as reader:
    left = list()
    right = list()
    for l, r in reader.iter_split("   ", int, int):
        left.append(l)
        right.append(r)

left_unique = set(left)
counts = {left: right.count(left) for left in left_unique}

total = 0
for l in left:
    total += l * counts[l]

print("Part 2:", total)

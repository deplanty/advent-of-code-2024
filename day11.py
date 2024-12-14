from src import Debug, Reader


def stone_evolve(stone: int) -> list:
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        tmp = str(stone)
        s1 = int(tmp[:len(tmp) // 2])
        s2 = int(tmp[len(tmp) // 2:])
        return [s1, s2]
    else:
        return [stone * 2024]


def blink(line: list) -> list:
    new_line = list()
    for stone in line:
        new_stones = stone_evolve(stone)
        new_line.extend(new_stones)
    return new_line


def blink_opti(stones: dict[int, int]) -> dict:
    new_stones = dict()
    for stone, qty in stones.items():
        created = stone_evolve(stone)
        for s in created:
            if s not in new_stones:
                new_stones[s] = 0
            new_stones[s] += qty
    return new_stones


debug = Debug()
example = False
debug.disable()

## Part 1

with Reader(11, example) as reader:
    line = reader.get_line(" ", int)

debug(0, line)

blinking = 25
for i in range(blinking):
    line = blink(line)
    debug(i + 1, line)

total = len(line)
print("Part 1:", total)

## Part 2

with Reader(11, example) as reader:
    line = reader.get_line(" ", int)

stones = dict()
for stone in line:
    if stone not in stones:
        stones[stone] = 0
    stones[stone] += 1

# debug.enable()
debug(0, stones)

blinking = 75
for i in range(blinking):
    stones = blink_opti(stones)
    debug(i + 1, stones)

total = sum(stones.values())
print("Part 2:", total)

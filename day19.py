import functools

from src import Debug, Reader, Chrono


debug = Debug()
example = False

with Reader(19, example) as reader:
    patterns = tuple(reader.get_line(", "))
    reader.raw_line()
    designs = [line for line in reader.iter_lines()]


## Part 1


@functools.cache
def find_design(patterns: list[str], design: str) -> int:
    res = 0
    for pattern in patterns:
        if design.startswith(pattern):
            if len(design) == len(pattern):
                return 1
            else:
                res += find_design(patterns, design[len(pattern) :])
    if res > 0:
        return 1
    else:
        return 0

chrono = Chrono()
total = 0
for design in designs:
    total += find_design(patterns, design)
print(chrono.text)
print("Part 1:", total)

## Part 2


@functools.cache
def find_all_design(patterns: list[str], design: str) -> int:
    res = 0
    for pattern in patterns:
        if design.startswith(pattern):
            if len(design) == len(pattern):
                res += 1
            else:
                res += find_all_design(patterns, design[len(pattern) :])
    return res


debug.disable()
chrono.start()
total = 0
for design in designs:
    qty = find_all_design(patterns, design)
    total += qty
    debug(f"Design: {design}\nN = {qty}")
    debug()
print(chrono.text)
print("Part 2:", total)

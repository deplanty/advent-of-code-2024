import re

from src import Debug, Reader, Index


def solve(ba: Index, bb: Index, prize: Index) -> tuple[float]:
    ay, ax = ba.ij
    by, bx = bb.ij
    py, px = prize.ij

    b = (py * ax - px * ay) / (ax * by - ay * bx)
    a = (px * by - py * bx) / (ax * by - ay * bx)
    return a, b


debug = Debug()
example = False

debug.disable()

pattern_button = re.compile(r"Button \w: X\+(?P<x>\d+), Y\+(?P<y>\d+)")
pattern_prize = re.compile(r"Prize: X=(?P<x>\d+), Y=(?P<y>\d+)")

with Reader(13, example) as reader:
    games: list[tuple[Index]] = list()
    blank = "\n"
    while blank == "\n":
        button_a = reader.one_line()
        match = pattern_button.match(button_a)
        button_a = Index(match.group("x"), match.group("y"))

        button_b = reader.one_line()
        match = pattern_button.match(button_b)
        button_b = Index(match.group("x"), match.group("y"))

        prize = reader.one_line()
        match = pattern_prize.match(prize)
        prize = Index(match.group("x"), match.group("y"))

        games.append((button_a, button_b, prize))

        blank = reader.raw_line()

## Part 1

total = 0
for i, (ba, bb, prize) in enumerate(games):
    debug(f"Game #{i + 1}")
    a, b = solve(ba, bb, prize)
    check = a * ba + b * bb

    if a.is_integer() and b.is_integer():
        total += int(a * 3 + b)

    debug(f"a = {a}, b = {b}")
    debug(f"Check: {check}")
    debug()

print("Part 1:", total)

## Part 2

pad = 10000000000000

total = 0
for i, (ba, bb, prize) in enumerate(games):
    prize.i += pad
    prize.j += pad

    debug(f"Game #{i + 1}")
    a, b = solve(ba, bb, prize)
    check = a * ba + b * bb

    if a.is_integer() and b.is_integer():
        total += int(a * 3 + b)

    debug(f"a = {a}, b = {b}")
    debug(f"Check: {check}")
    debug()

print("Part 2:", total)

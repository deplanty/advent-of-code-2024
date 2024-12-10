import copy
import itertools

from src.reader import Reader


example = False

## Part 1


def calc(val1: int, op: str, val2: int):
    if op == "+":
        return val1 + val2
    elif op == "*":
        return val1 * val2


with Reader(7, example) as reader:
    calibrations = dict()
    for line in reader.iter_lines():
        res, val = line.split(": ")
        calibrations[int(res)] = [int(v) for v in val.split(" ")]


total = 0
for result, values in calibrations.items():
    operations = itertools.product("+*", repeat=len(values) - 1)
    for sequence in operations:
        values_tmp = copy.deepcopy(values)
        for op in sequence:
            val1 = values_tmp.pop(0)
            val2 = values_tmp.pop(0)
            test = calc(val1, op, val2)
            values_tmp.insert(0, test)

        if test == result:
            total += result
            break

print("Part 1:", total)

## Part 2


def calc2(val1: int, op: str, val2: int):
    if op == "+":
        return val1 + val2
    elif op == "*":
        return val1 * val2
    elif op == "|":
        return int(str(val1) + str(val2))


total = 0
for result, values in calibrations.items():
    operations = itertools.product("+*|", repeat=len(values) - 1)
    for sequence in operations:
        values_tmp = copy.deepcopy(values)
        for op in sequence:
            val1 = values_tmp.pop(0)
            val2 = values_tmp.pop(0)
            test = calc2(val1, op, val2)
            values_tmp.insert(0, test)

        if test == result:
            total += result
            break

print("Part 2:", total)

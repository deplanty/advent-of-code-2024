import copy

from src.reader import Reader
from src import utils

## Part 1

def is_ok(diff: int, sign:int) -> bool:
    # Monotonous and small variation (<= 3)
    return diff != 0 and utils.sign(diff) == sign and abs(diff) <= 3


def is_line_safe(line: list):
    # Init
    safe = True
    sign = utils.sign(line[1] - line[0])
    # Check all the values
    for i in range(len(line) - 1):
        diff = line[i + 1] - line[i]
        if not is_ok(diff, sign):
            safe = False
            break
        sign = utils.sign(diff)

    return safe


with Reader(2) as reader:
    total = 0
    for line in reader.iter_split(" ", int):
        if is_line_safe(line):
            total += 1

print("Part 1:", total)

## Part 2

fid = open("test/day2p2.txt", "w")

count = 0
with Reader(2) as reader:
    total = 0
    # For each line of the file
    for line in reader.iter_split(" ", int):
        count += 1
        # If the report is safe (monotonous and no variation > 3)
        if is_line_safe(line):
            print(line, "SAFE")
            print("F", *line, file=fid)
            total += 1
        # If the report is not safe
        else:
            print(line, "UNSAFE")
            # For each level in the report
            for i in range(len(line)):
                # Remove a level
                line_tmp = copy.copy(line)
                line_tmp.pop(i)
                print(line, line_tmp)
                # Check if the report without this level is safe
                if is_line_safe(line_tmp):
                    print("SAFE")
                    print("D", *line, file=fid)
                    total += 1
                    break
            else:
                print("UNSAFE")

fid.close()
print("Part 2:", total, "/", count)

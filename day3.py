import re

from src.reader import Reader


example = False


## Part 1

pattern_mul = re.compile(r"mul\((\d+),(\d+)\)")

with Reader(3, example) as reader:
    total = 0
    for line in reader.iter_lines():
        results = pattern_mul.findall(line)
        for a, b in results:
            total += int(a) * int(b)

print("Part 1:", total)

## Part 2

pattern_detect = re.compile(r"(mul\(\d+,\d+\)|do\(\)|don\'t\(\))")

with Reader(3, example) as reader:
    total = 0
    enabled = True
    for line in reader.iter_lines():
        results = pattern_detect.findall(line)
        for detect in results:
            if detect == "don't()":
                enabled = False
            elif detect == "do()":
                enabled = True
            elif enabled:
                find = pattern_mul.match(detect)
                a = int(find.group(1))
                b = int(find.group(2))
                total += a * b

print("Part 2:", total)

import re

from src import Debug, Reader


debug = Debug()
example = True


def calculate(values: dict[str, int], var1: int, operation: str, var2: int) -> int:
    val1 = values[var1]
    val2 = values[var2]
    if operation == "AND":
        return val1 and val2
    elif operation == "OR":
        return val1 or val2
    elif operation == "XOR":
        return val1 ^ val2
    else:
        raise ValueError(f"Unknow operation '{operation}'.")


pattern_values = re.compile(r"(\w+): (\d)")
pattern_operations = re.compile(r"(\w+) (\w+) (\w+) -> (\w+)")

with Reader(24, example) as reader:
    init_values, init_operations = reader.read().split("\n\n")

    values: dict[str, int] = {name: int(value) for name, value in pattern_values.findall(init_values)}
    operations: list[tuple[str]] = pattern_operations.findall(init_operations)

## Part 1

N = len(operations)
for i, (var1, op, var2, res) in enumerate(operations, 1):
    debug(f"Operation {i}/{N}")
    value = calculate(values, var1, op, var2)
    values[res] = value

pattern_var = re.compile(r"z(\d+)")

total = 0
for name, value in values.items():
    match = pattern_var.match(name)
    if match:
        bit = match.group(1)
        debug(bit)

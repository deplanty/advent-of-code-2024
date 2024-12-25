import re

from src import Debug, Reader


debug = Debug()
example = False


def calculate(
    var1: str, operation: str, var2: str, res: str, cache: dict[str, int]
) -> int:
    # Retrieve data from previous calcs
    if var1 in cache:
        val1 = cache[var1]
    else:
        v1, op, v2 = operations[var1]
        val1 = calculate(v1, op, v2, var1, cache)

    if var2 in cache:
        val2 = cache[var2]
    else:
        v1, op, v2 = operations[var2]
        val2 = calculate(v1, op, v2, var2, cache)

    # Process calc with the data
    if operation == "AND":
        result = val1 and val2
    elif operation == "OR":
        result = val1 or val2
    elif operation == "XOR":
        result = val1 ^ val2
    else:
        raise ValueError(f"Unknow operation '{operation}'.")

    values[res] = result
    return result


pattern_values = re.compile(r"(\w+): (\d)")
pattern_operations = re.compile(r"(\w+) (\w+) (\w+) -> (\w+)")

with Reader(24, example) as reader:
    init_values, init_operations = reader.read().split("\n\n")

    values: dict[str, int] = {
        name: int(value) for name, value in pattern_values.findall(init_values)
    }
    operations_tmp: list[tuple[str]] = pattern_operations.findall(init_operations)


operations: dict[str, tuple[str]] = dict()
for var1, op, var2, res in operations_tmp:
    operations[res] = (var1, op, var2)

## Part 1

debug.disable()

pattern_var = re.compile(r"z(\d+)")
N = len(operations)
total = 0
for i, (res, (var1, op, var2)) in enumerate(operations.items(), 1):
    debug(f"Operation {i}/{N}")
    match = pattern_var.match(res)
    if match:
        debug(res)
        bit = match.group(1)
        value = calculate(var1, op, var2, res, values)
        debug(int(bit), value, value * pow(2, int(bit)))
        total += value * pow(2, int(bit))

print("Part 1:", total)

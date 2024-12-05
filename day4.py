from src.index import Index
from src.reader import Reader



example = False

## Part 1

def count_xmas(table:list, index:Index) -> int:
    """
    Count the number of time a XMAS appears from the position.
    """
    def check(table:list, index:Index, value:str) -> bool:
        if index.is_in(table):
            return index.get(table) == value

    if index.get(table) != "X":
        return 0
    else:
        count = 0
        for direction in index.get_directions_8():
            # Check M
            neig = index + direction
            if not check(table, neig, "M"):
                continue
            # Check A
            neig = neig + direction
            if not check(table, neig, "A"):
                continue
            # Check S
            neig = neig + direction
            if not check(table, neig, "S"):
                continue
            # XMAS found!
            count += 1
        return count


with Reader(4, example) as reader:
    table = reader.get_table("")

# Detect all the X

total = 0
for i, line in enumerate(table):
    for j, char in enumerate(line):
        total += count_xmas(table, Index(i, j))

print("Part 1:", total)


## Part 2

def count_mas(table:list, index:Index) -> int:
    """
    Count the number of time a MAS appears from the position.
    """

    def check(table:list, index:Index, value:str) -> bool:
        if index.is_in(table):
            return index.get(table) == value
        else:
            return False

    if index.get(table) != "A":
        return 0
    else:
        count = 0
        # Check Diag ↘
        if check(table, index.NW, "M") and check(table, index.SE, "S"):
            count += 1
        # Check Diag ↖
        elif check(table, index.NW, "S") and check(table, index.SE, "M"):
            count += 1

        # Check Diag ↙
        if check(table, index.NE, "M") and check(table, index.SW, "S"):
            count += 1
        # Check Diag ↗
        elif check(table, index.NE, "S") and check(table, index.SW, "M"):
            count += 1

        if count == 2:
            return 1
        else:
            return 0


with Reader(4, example) as reader:
    table = reader.get_table("")

# Detect all the X

total = 0
for i, line in enumerate(table):
    for j, char in enumerate(line):
        total += count_mas(table, Index(i, j))

print("Part 2:", total)

DEBUG = True


def _file_from_day(day:int, example:bool=False) -> str:
    if example:
        return f"inputs/day{day}ex.txt"
    else:
        return f"inputs/day{day}.txt"


def read_lines(day, example=False) -> list[str]:
    file = _file_from_day(day, example)

    with open(file, "r", encoding="utf-8") as fid:
        return fid.read().splitlines()


def iter_lines(day, example=False) -> str:
    file = _file_from_day(day, example)

    with open(file, "r", encoding="utf-8") as fid:
        for line in fid:
            if line.startswith("--STOP--"):
                return
            yield line.rstrip().split()


def read(day, example=False) -> str:
    file = _file_from_day(day, example)
    with open(file, "r", encoding="utf-8") as fid:
        return fid.read()


def read_table(day, example=False) -> list:
    table = list()
    for line in iter_lines(day, example):
        table.append(list(line))
    return table


def read_table_int(day, example=False) -> list:
    """
    Return the input file as a table of int.
    """

    table = list()
    for line in iter_lines(day, example):
        table.append([int(x) for x in line])
    return table


def transpose(table:list[list]):
    return [list(x) for x in zip(*table)]


def show_table(table):
    for line in table:
        print("".join([str(x) for x in line]))


def show_table_int(table):
    maxi = [0 for j in range(len(table[0]))]
    for i in range(len(table)):
        for j in range(len(table[0])):
            maxi[j] = max(maxi[j], len(str(table[i][j])))

    for i in range(len(table)):
        for j in range(len(table[0])):
            print(f"{table[i][j]:>{maxi[j] + 1}}", end="")
        print()


def is_in_bound(table, i, j):
    rows = len(table)
    cols = len(table)
    return 0 <= i < rows and 0 <= j < cols


def p(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def prepare(day:int):
    import os

    def create_file(file):
        if not os.path.exists(file):
            open(file, "w", encoding="utf-8").close()
    # Python file
    create_file(f"day{day}.py")
    create_file(f"inputs/day{day}.txt")
    create_file(f"inputs/day{day}ex.txt")


def sign(value: int) -> int:
    """Return the sign of a value as -1, 0 or 1"""

    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0




if __name__ == "__main__":
    prepare(4)

class Reader:
    def __init__(self, day: int, example: bool = False):
        if example:
            self.filename = f"inputs/day{day}ex.txt"
        else:
            self.filename = f"inputs/day{day}.txt"

        self.fid = None

    def __enter__(self) -> "Reader":
        self.fid = open(self.filename, "r")
        return self

    def __exit__(self, *args):
        self.fid.close()

    def _iter_lines(self) -> str:
        for line in self.fid:
            if line.startswith("--STOP--"):
                return
            yield line.rstrip()

    def _split(self, line: str, separator: str = " ") -> list:
        return line.split(separator)

    def one_line(self) -> str:
        """
        Return one line of the file.
        """

        return self.fid.readline().rstrip()

    def iter_lines(self, type=str) -> list:
        """
        Yield one line after the other.
        """

        for line in self._iter_lines():
            yield type(line)

    def iter_split(self, separator: str = " ", *types) -> list:
        """
        Yield a list of the next line and extract the given types.

        Examples:
            ```python
            # Each line of the file is "string string"
            reader.iter_split(" ")
            # Each line of the file is "int float int"
            reader.iter_split(" ", int, float, int)
            # Each line of the file is "int int int"
            reader.iter_split(" ", int)
            ```
        """

        for line in self._iter_lines():
            line = self._split(line, separator)
            if not types:
                yield line
            else:
                if len(types) == 1:
                    t = types[0]
                    yield [t(value) for value in line]
                else:
                    yield [t(value) for value, t in zip(line, types)]

    def get_table(self, separator: str = " ", *types) -> list[list]:
        """
        Return a table of the given types.

        Examples:
            ```python
            # Each line of the file is "string string"
            reader.get_table(" ")
            # Each line of the file is "int float int"
            reader.get_table(" ", int, float, int)
            # Each line of the file is "int int int"
            reader.get_table(" ", int)
            ```
        """

        if separator is None:
            return [line for line in self.iter_lines()]
        elif separator == "":
            return [list(line) for line in self.iter_lines()]
        else:
            return [line for line in self.iter_split(separator, *types)]

    def get_field(self, separator: str = " ", type=str) -> list[list]:
        """
        Return a table where each cell has the given type.
        """

        return [[type(x) for x in line] for line in self.iter_lines()]

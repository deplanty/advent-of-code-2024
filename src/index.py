class Index:
    """
    An index position to manage the positions in a table object (list[list]).

    Args:
        i (int): the row position.
        j (int): the column position.
    """

    def __init__(self, i:int, j:int):
        self.i = i
        self.j = j

    def __eq__(self, other:"Index") -> bool:
        return self.i == other.i and self.j == other.j

    def __add__(self, other:"Index") -> "Index":
        return Index(self.i + other.i, self.j + other.j)

    def __hash__(self):
        return hash(self.ij)

    def __str__(self):
        return str(self.ij)

    def __repr__(self):
        return str(self)

    # Properties

    @property
    def ij(self):
        return self.i, self.j

    @property
    def N(self):
        return Index(self.i - 1, self.j)

    @property
    def S(self):
        return Index(self.i + 1, self.j)

    @property
    def W(self):
        return Index(self.i, self.j - 1)

    @property
    def E(self):
        return Index(self.i, self.j + 1)

    @property
    def NW(self):
        return Index(self.i - 1, self.j - 1)

    @property
    def NE(self):
        return Index(self.i - 1, self.j + 1)

    @property
    def SW(self):
        return Index(self.i + 1, self.j - 1)

    @property
    def SE(self):
        return Index(self.i + 1, self.j + 1)

    @property
    def NESW(self):
        return self.N, self.E, self.S, self.W

    @property
    def delta_N(self):
        return Index(-1, 0)

    @property
    def delta_S(self):
        return Index(1, 0)

    @property
    def delta_W(self):
        return Index(0, -1)

    @property
    def delta_E(self):
        return Index(0, 1)

    @property
    def delta_NW(self):
        return Index(-1, -1)

    @property
    def delta_NE(self):
        return Index(-1, 1)

    @property
    def delta_SW(self):
        return Index(1, -1)

    @property
    def delta_SE(self):
        return Index(1, 1)

    # Methods

    def get_neighbours_4(self) -> list["Index"]:
        """
        Return the indices of the 4 direct neighbours from the current index.
        """

        return [self.N, self.E, self.S, self.W]

    def get_neighbours_8(self) -> list["Index"]:
        """
        Return the indices of the 8 direct neighbours from the current index.
        """

        return [self.N, self.NE, self.E, self.SE, self.S, self.SW, self.W, self.NW]

    def get_diagonal(self) -> list["Index"]:
        """
        Return all the indices in diagonal from the current index.
        """

        return [self.NE, self.SE, self.SW, self.NW]

    def get_directions_8(self) -> list["Index"]:
        """
        Return the direction to move from the current position to the 8 neighbours.
        """

        return [self.delta_N, self.delta_NE, self.delta_E, self.delta_SE, self.delta_S, self.delta_SW, self.delta_W, self.delta_NW]

    def get(self, table:list):
        """
        Return the value of the table at the current index.
        """

        return table[self.i][self.j]

    def is_in(self, table:list):
        rows = len(table)
        cols = len(table[0])
        return 0 <= self.i < rows and 0 <= self.j < cols

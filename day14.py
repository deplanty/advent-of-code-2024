from src import Debug, Reader, Index


class Robot:
    __iid = 0

    def __init__(self, position: Index, velocity: Index):
        self.position = position
        self.velocity = velocity

        self.iid = self.__iid
        self.__iid += 1

    def __str__(self) -> str:
        return f"Robot #{self.iid} @{self.position} v{self.velocity}"

    def __repr__(self) -> str:
        return str(self)

    def move(self, seconds: int = 1):
        self.position += seconds * self.velocity

    def fit(self, size: Index):
        self.position.i %= size.i
        self.position.j %= size.j


debug = Debug()
example = False

robots: list[Robot] = list()
with Reader(14, example) as reader:
    for position, velocity in reader.iter_split():
        px, py = position[2:].split(",")
        vx, vy = velocity[2:].split(",")

        robots.append(Robot(Index(py, px), Index(vy, vx)))

size: Index = {
    True: Index(7, 11),  # Example size
    False: Index(103, 101),  # Input size
}.get(example)

for robot in robots:
    robot.move(100)
    robot.fit(size)
    debug(robot)
debug()

quadrant = {
    "nw": 0,
    "ne": 0,
    "se": 0,
    "sw": 0,
}
for robot in robots:
    corner = ""

    if robot.position.j < size.j // 2:
        corner += "n"
    elif robot.position.j > size.j // 2:
        corner += "s"

    if robot.position.i < size.i // 2:
        corner += "w"
    elif robot.position.i > size.i // 2:
        corner += "e"

    debug(robot, corner)
    if corner in quadrant:
        quadrant[corner] += 1

total = 1
for count in quadrant.values():
    total *= count
print("Part 1:", total)
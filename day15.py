from src import Debug, Reader, Index


debug = Debug()
example = False

WALL = "#"
EMPTY = "."
BOX = "O"
ROBOT = "@"
BOX_L, BOX_R = "[", "]"

## Part 1

debug.disable()

def move_in_field(field: list[list[str]], source: Index, delta: Index):
    """
    Move the element at position `source` with a `delta` displancement.
    """

    destination = source + delta
    s = source.get(field)
    source.set(field, EMPTY)
    destination.set(field, s)


robot: Index = Index(0, 0)
field: list[list[str]] = list()
moves: str = str()
with Reader(15, example) as reader:
    state = "field"
    for i, line in enumerate(reader.iter_lines()):
        if state == "field":
            if line == "":
                state = "moves"
                continue
            if "@" in line:
                j = line.index("@")
                robot = Index(i, j)
            field.append(list(line))
        elif state == "moves":
            moves += line
            pass

debug("Field")
debug.show_field(field)
debug()
debug("Moves")
debug(moves)
debug()
debug(f"Robot : {robot}")
debug()

delta = {
    "^": Index.delta_N,
    ">": Index.delta_E,
    "v": Index.delta_S,
    "<": Index.delta_W,
}

for move in moves:
    d = delta.get(move)
    target = robot + d
    # Wall: do nothing
    if target.get(field) == WALL:
        continue
    # Empty: move the robot
    elif target.get(field) == EMPTY:
        move_in_field(field, robot, d)
        robot += d
    # Box: move the box and all the boxes in the direction
    elif target.get(field) == BOX:
        boxes: list[Index] = list()
        while target.get(field) == BOX:
            boxes.append(target)
            target += d
        debug(boxes)

        # Move all the boxes if the last one is next to an empty space
        # Move the robot after
        target = boxes[-1] + d
        if target.get(field) == EMPTY:
            for i in range(len(boxes) - 1, -1, -1):
                box = boxes[i]
                move_in_field(field, box, d)
            move_in_field(field, robot, d)
            robot += d

    debug.show_field(field)

# Calculate the GPS for all the boxes
total = 0
for i, line in enumerate(field):
    for j, element in enumerate(line):
        index = Index(i, j)
        if index.get(field) == BOX:
            total += 100 * index.i + index.j
print("Part 1:", total)

## Part 2

debug.disable()


def get_box_twin(field: list[list[str]], index: Index) -> Index:
    """From a position, return the position of the other side of the box"""

    if index.get(field) == BOX_L:
        return index.E
    elif index.get(field) == BOX_R:
        return index.W


robot: Index = Index(0, 0)
field: list[list[str]] = list()
moves: str = str()
with Reader(15, example) as reader:
    state = "field"
    for i, line in enumerate(reader.iter_lines()):
        # When we are looking at the input field
        if state == "field":
            if line == "":
                state = "moves"
                continue
            # For each line of the input, change the char by two others
            field_line: list[str] = list()
            for j, char in enumerate(line):
                if char == WALL:
                    field_line.extend([WALL, WALL])
                elif char == BOX:
                    field_line.extend([BOX_L, BOX_R])
                elif char == EMPTY:
                    field_line.extend([EMPTY, EMPTY])
                elif char == ROBOT:
                    field_line.extend([ROBOT, EMPTY])
            # Locate the robot in the field
            if ROBOT in field_line:
                j = field_line.index(ROBOT)
                robot = Index(i, j)
            # Add the line to the complete field
            field.append(field_line)
        # When we are looking at the input moves
        elif state == "moves":
            moves += line
            pass

debug("Moves")
debug(moves)
debug()
debug(f"Robot : {robot}")
debug()
debug("Field")
debug.show_field(field)
debug()


delta = {
    "^": Index.delta_N,
    ">": Index.delta_E,
    "v": Index.delta_S,
    "<": Index.delta_W,
}

for i, move in enumerate(moves):
    debug()
    debug(f"Move: {move}")
    debug.input(f"{i+1}/{len(moves)}")

    d = delta.get(move)
    target = robot + d
    # Wall: do nothing
    if target.get(field) == WALL:
        pass
    # Empty: move the robot
    elif target.get(field) == EMPTY:
        move_in_field(field, robot, d)
        robot += d
    # Box: move the box and all the boxes in the direction
    elif target.get(field) in [BOX_L, BOX_R]:
        boxes: list[Index] = [target, get_box_twin(field, target)]
        targets: list[Index] = [target, get_box_twin(field, target)]
        # Get all the movable boxes
        while targets:
            next_targets: list[Index] = list()
            for box in targets:
                target = box + d
                if target in boxes:
                    continue
                if target.get(field) in [BOX_L, BOX_R]:
                    next_targets.extend([target, get_box_twin(field, target)])
                    boxes.extend([target, get_box_twin(field, target)])
            targets = next_targets
        debug(boxes)

        # Check if the boxes can be moved
        can_move = True
        for box in boxes:
            target = box + d
            if target.get(field) == WALL:
                can_move = False


        # Move all the boxes if the last ones is next to an empty space
        # Move the robot after
        if can_move:
            for i in range(len(boxes) - 1, -1, -1):
                box = boxes[i]
                move_in_field(field, box, d)
            move_in_field(field, robot, d)
            robot += d

    debug.show_field(field)

# debug.enable()
# debug.show_field(field)

# Calculate the GPS for all the boxes
total = 0
for i, line in enumerate(field):
    for j, element in enumerate(line):
        index = Index(i, j)
        if index.get(field) == BOX_L:
            total += 100 * index.i + index.j
print("Part 2:", total)

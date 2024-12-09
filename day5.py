from src.reader import Reader


example = False

## Part 1

with Reader(5, example) as reader:
    state = "order"

    # The data is separated in 2 parts
    # 1. Orders
    # 2. Updates
    list_order = list()
    list_update = list()
    for line in reader.iter_lines():
        if line == "":
            state = "update"
            continue

        if state == "order":
            x, y = line.split("|")
            list_order.append((int(x), int(y)))
        elif state == "update":
            line = line.split(",")
            list_update.append([int(x) for x in line])

# Restructure the orders
order = dict()
for x, y in list_order:
    if x not in order:
        order[x] = {"before": list(), "after": list()}
    if y not in order[x]["before"]:
        order[x]["before"].append(y)

    if y not in order:
        order[y] = {"before": list(), "after": list()}
    if x not in order[y]["after"]:
        order[y]["after"].append(x)


# Process the updates
# - Get which are correct and which are incorrect
total = 0
update_incorrect = list()
for update in list_update:
    good = True
    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            x, y = update[i], update[j]
            if y not in order[x]["before"]:
                # print(f"{update} not good: x={x} and y={y}")
                good = False
                update_incorrect.append(update)
                break
        if not good:
            break

    if good:
        middle = update[len(update) // 2]
        # print(f"{update} good: {middle}")
        total += middle

print("Part 1:", total)


## Part 2


def insert(array: list, value: int):
    """
    Insert the value in the update at the correct position.
    """

    global order

    for i, x in enumerate(array):
        if value in order[x]["after"]:
            array.insert(i, value)
            break
    else:
        array.append(value)


total = 0
for update in update_incorrect:
    ordered = list()
    for element in update:
        insert(ordered, element)
        pass

    # print(ordered)
    middle = ordered[len(ordered) // 2]
    total += middle

print("Part 2:", total)

from src.reader import Reader


example = True

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
for update in list_update:
    total = 0
    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            x, y = update[i], update[j]
            if y not in order[x]["before"]:
                print(x, y, "NOT GOOD")


print("Part 1:", total)

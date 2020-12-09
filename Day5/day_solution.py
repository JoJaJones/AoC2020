from util import *

data = load_and_parse("data.txt")

def find_coord(data, val_range, high_marker):
    min_val, max_val = val_range
    last_val = False
    for idx, char in enumerate(data):
        if idx == len(data) - 1:
            last_val = True
        if char == high_marker:
            min_val = (min_val + max_val) // 2 + 1
            if last_val:
                return min_val
        else:
            max_val = (min_val + max_val) // 2
            if last_val:
                return max_val

def calculate_id(row, col):
    return row*8 + col

def part_one(data):
    max_id = 0
    for entry in data:
        entry_id = calculate_id(find_coord(entry[:-3], (0, 127), "B"), find_coord(entry[-3:], (0, 7), "R"))
        if entry_id > max_id:
            max_id = entry_id

    return max_id

def part_two(data):
    ids = []
    for entry in data:
        ids.append(calculate_id(find_coord(entry[:-3], (0, 127), "B"), find_coord(entry[-3:], (0, 7), "R")))

    ids.sort()
    prev = ids[0]
    potentials = []
    for idx in range(1, len(ids)):
        cur = ids[idx]
        if cur != prev + 1:
            potentials.append(cur - 1)

        prev = cur
    return potentials



print(part_one(data))
print(part_two(data))
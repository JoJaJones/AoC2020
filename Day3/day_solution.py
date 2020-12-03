from util import load_and_parse

def parse_function(line):
    return line.strip()

data = load_and_parse("data.txt", parse_function)

def part_one(data):
    c_idx = 0
    count = 0
    for row in data:
        if row[c_idx] == "#":
            count += 1
        # print(row[c_idx], count)
        c_idx += 3
        c_idx %= len(row)

    return calc_collisions((3, 1), data)

def calc_collisions(slope, data):
    r_idx = 0
    c_idx = 0
    c_shift, r_shift = slope
    count = 0
    while r_idx < len(data):
        if data[r_idx][c_idx] == "#":
            count += 1
        r_idx += r_shift
        c_idx = (c_idx + c_shift) % len(data[0])

    return count

def part_two(data):
    collisions = []
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        collisions.append(calc_collisions(slope, data))

    mult = collisions.pop()
    while len(collisions) > 0:
        mult *= collisions.pop()

    return mult

print(part_two(data))
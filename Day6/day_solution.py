from util import *

data = load_and_parse("data.txt")

def group_data(raw_data):
    data = [[]]
    for line in raw_data:
        if len(line.strip()) == 0:
            data.append([])
        else:
            data[-1].append(line.strip())

    return data

grouped_data = group_data(data)

def part_one(raw_data):
    count = 0
    for line in raw_data:
        count += len(set([char for char in "".join(line)]))

    return count

def part_two(data):
    count = 0
    for group in data:
        unanimouses = set([char for char in group[0]])
        for idx in range(1, len(group)):
            unanimouses = unanimouses.intersection(set([char for char in group[idx]]))

        count += len(unanimouses)

    return count


print(part_one(grouped_data))
print(part_two(grouped_data))
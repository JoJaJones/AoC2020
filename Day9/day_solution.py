import time

from util import load_and_parse

def parse_function(line):
    return int(line)

data = load_and_parse("data.txt", parse_function)

def part_one(data):
    l = []
    for val in data:
        if len(l) < 25:
            l.append(val)
        else:
            if find_val(val, data):
                l.pop(0)
                l.append(val)
            else:
                return val

# def find_val(val, data):
#     for i in range(len(data)):
#         for j in range(len(data)):
#             if i != j and data[i] + data[j] == val:
#                 return True
#
#     return False

def find_val(val, data):
    two_sum = {}
    for num in data:
        if num in two_sum:
            return True
        else:
            two_sum[val-num] = num

    return False

def part_two(data, target):
    start = 0
    end = start
    total = 0
    l = []
    while end < len(data) and total < target:
        total += data[end]
        l.append(data[end])
        end += 1
        while total > target:
            total -= data[start]
            start += 1
            l.pop(0)

    l.sort()
    return l[0] + l[-1]

start = time.perf_counter()
target = part_one(data)
print(target)
print(part_two(data, target))
end = time.perf_counter()
print(end-start)

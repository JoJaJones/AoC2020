from util import load_and_parse

def parse_line(line):
    count_range, ltr, pwrd = line.split(" ")
    low_val, high_val = [int(x) for x in count_range.split("-")]
    ltr = ltr[0]
    return (low_val, high_val, ltr, pwrd)

def part_one(data):

    valid_count = 0
    for val in data:
        low, high, ltr, pwrd = val
        if low <= pwrd.count(ltr) <= high:
            valid_count += 1

    return valid_count

def part_two(data):
    valid_count = 0
    for val in data:
        low, high, ltr, pwrd = val

        low_is = pwrd[low - 1] == ltr
        high_is = pwrd[high - 1] == ltr
        if low_is ^ high_is:
            valid_count += 1

    return valid_count

data = load_and_parse("data.txt", parse_line)

print(part_one(data))
print(part_two(data))
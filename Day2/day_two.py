from util import load_array

arr = load_array("data.txt")
valid_count = 0
for val in arr:
    count_range, ltr, pwrd = val.split(" ")
    low_val, high_val = [int(x) for x in count_range.split("-")]
    ltr = ltr[0]
    low_is = pwrd[low_val - 1] == ltr
    high_is = pwrd[high_val - 1] == ltr
    if  low_is ^ high_is:
        valid_count += 1

print(valid_count)
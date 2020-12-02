def load_array():
    arr = []
    with open("expenses.txt", "r") as infile:
        for line in infile:
            line = int(line)
            arr.append(line)

    return arr

def find_two_2020():
    two_sum = {}
    arr = load_array()
    for val in arr:
        if val in two_sum:
            return val, two_sum[val]
        else:
            two_sum[2020-val] = val

def find_three_2020():
    arr = sorted(list(set(load_array())))
    print(arr)
    for i, a in enumerate(arr):
        l, r = i+1, len(arr) - 1
        while l < r:
            three_sum = a + arr[l] + arr[r]
            if three_sum > 2020:
                r -= 1
            elif three_sum < 2020:
                l += 1
            else:
                return a, arr[l], arr[r]

def mult_two():
    a, b = find_two_2020()
    return a * b

def mult_three():
    a, b, c = find_three_2020()
    return a * b * c

print(mult_three())
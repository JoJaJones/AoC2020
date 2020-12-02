def load_array(file_name):
    arr = []
    with open(file_name, "r") as infile:
        for line in infile:
            arr.append(line)

    return arr

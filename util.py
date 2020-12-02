def load_array(file_name):
    arr = []
    with open(file_name, "r") as infile:
        for line in infile:
            arr.append(line)

    return arr

def default_parse(line):
    return line

def load_and_parse(file_name: str, parse_func=default_parse) -> list:
    arr = []
    with open(file_name, "r") as infile:
        for line in infile:
            arr.append(parse_func(line))

    return arr


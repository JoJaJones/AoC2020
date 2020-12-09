def load_array(file_name):
    arr = []
    with open(file_name, "r") as infile:
        for line in infile:
            arr.append(line)

    return arr

def default_parse_str(line, strip_it=True):
    return line.strip() if strip_it else line

def default_parse_int(line):
    return int(line)

def load_and_parse(file_name: str, parse_func=default_parse_str) -> list:
    arr = []
    with open(file_name, "r") as infile:
        for line in infile:
            arr.append(parse_func(line))

    return arr
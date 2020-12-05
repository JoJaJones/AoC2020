from passport_validator import *

color_hex_validator = content_validator({range(1): "#", range(1, 7): "abcdef1234567890"}, 7)
print(color_hex_validator("#000000"))

from util import *
from passport_validator import *

def parse_function(data):
    new_list = []
    idx = 0
    while idx < len(data):
        if idx == 0:
            new_list.append(data[idx] + " ")
        elif len(data[idx]) == 0:
            new_list.append("")
        else:
            new_list[-1] += data[idx] + " "
        idx += 1

    return new_list

data = parse_function(load_and_parse("data.txt"))

def complete_pass(pass_dict):
    if len(pass_dict) == 8:
        return True

    if len(pass_dict) == 7 and "cid" not in pass_dict:
        return True

    return False

validation_reqs = {
    BYR: number_validator((1920, 2002)),
    IYR: number_validator((2010, 2020)),
    EYR: number_validator((2020, 2030)),
    PID: content_validator({range(9): "0987654321"}, 9),
    HGT: measure_validator(-2, {"cm": (150, 193), "in": (59, 76)}),
    HCL: content_validator({range(1): "#", range(1, 7): "abcdef1234567890"}, 7),
    ECL: option_validator(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
    CID: optional_validator()
}

def validate_pass(pass_dict):
    if not complete_pass(pass_dict):
        return False

    try:
        byr = int(pass_dict["byr"])
        iyr = int(pass_dict["iyr"])
        eyr = int(pass_dict["eyr"])
        pid = int(pass_dict["pid"])
        hgt = int(pass_dict["hgt"][:-2])
    except:
        return False

    hcl = pass_dict["hcl"]
    if hcl[0] != "#":
        return False

    if not (1920 <= byr <= 2002):
        return False

    if not (2010 <= iyr <= 2020):
        return False

    if not (2020 <= eyr <= 2030):
        return False

    hgt_measure = pass_dict["hgt"][-2:]
    if hgt_measure not in ["in", "cm"]:
        return False

    if hgt_measure == "in" and not (59 <= hgt <= 76):
        return False

    if hgt_measure == "cm" and not (150 <= hgt <= 193):
        return False

    for i in range(1, len(hcl)):
        if hcl[i] not in "0987654321abcdef":
            return False

    if pass_dict["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    if len(pass_dict["pid"]) != 9:
        return False

    return True

def load_dict(raw_data):
    data = []
    for entry in raw_data:
        data.append({})
        for section in entry.strip().split(" "):
            key, value = section.split(":")
            data[-1][key] = value

    count = 0
    for entry in data:
        if complete_pass(entry):
            count += 1

    return count, data
print(data)
res, parsed_data = load_dict(data)

plist = PassportList(parsed_data, validation_reqs)

def part_two(data):
    valids = []
    for entry in data:
        if validate_pass(entry):
            valids.append(entry)

    # key = "hgt"
    # print_valids(sorted(valids, key= lambda data: data[key]), key)
    return len(valids)

def print_valids(data, key):
    for entry in data:
        print(entry[key])

print(part_two(parsed_data))
print(plist.count_valid())
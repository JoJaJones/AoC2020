BYR = "byr"
IYR = "iyr"
EYR = "eyr"
PID = "pid"
CID = "cid"
HGT = "hgt"
HCL = "hcl"
ECL = "ecl"


class Entry:
    def __init__(self, value, validator):
        self.data = value
        self.validator = validator

    def is_valid(self):
        return self.validator(self.data)


def suffix_validator(slice_idx, valid_suffixes):
    def validator(data):
        # try:
        #     val = int(data[:slice_idx])
        # except:
        #     return False

        suffix = data[slice_idx:]
        if suffix in valid_suffixes:
            # min_val, max_val = valid_range_dict[suffix]
            # return min_val <= max_val
            return True
        else:
            return False
    return validator


def number_validator(valid_range=None):
    def validator(data):
        try:
            data = int(data)
        except:
            return False

        if valid_range is None:
            return True
        else:
            min_val, max_val = valid_range
            return min_val <= data <= max_val

    return validator


def prefix_validator(slice_idx, valid_prefixes):
    def validator(data):
        if data[:slice_idx] in valid_prefixes:
            return True
        else:
            return False

    return validator


def length_validator(valid_length):
    def validator(data):
        return len(data) == valid_length

    return validator


def content_validator(valid_value_dict, length):
    def validator(data):
        len_validator = length_validator(length)
        if not len_validator(data):
            return False

        for key in valid_value_dict:
            for idx in key:
                if data[idx] not in valid_value_dict[key]:
                    return False

        return True

    return validator


def option_validator(valid_options):
    def validator(data):
        return data in valid_options

    return validator


def measure_validator(slice_idx, valid_range_dict):
    def validator(data):
        end_validator = suffix_validator(slice_idx, valid_range_dict.keys())
        if not end_validator(data):
            return False

        num_validator = number_validator(valid_range_dict[data[slice_idx:]])
        return num_validator(data[:slice_idx])

    return validator


def compound_validator(funcs):
    def validator(data):
        for func in funcs:
            if not func(data):
                return False

        return True

    return False


def optional_validator():
    def validator(data):
        return True

    return validator


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


class Passport:
    def __init__(self, entry_data, validation_requirements):
        self.entries = {}
        for section in entry_data:
            self.entries[section] = Entry(entry_data[section], validation_requirements[section])

    def is_valid(self):
        if not self.is_complete():
            return False

        for entry in self.entries:
            if not self.entries[entry].is_valid():
                return False

        return True

    def is_complete(self):
        if len(self.entries) == 8:
            return True

        if len(self.entries) == 7 and "cid" not in self.entries:
            return True

        return False

class PassportList:
    def __init__(self, data, validation_requirements):
        self.passports = []
        for entry in data:
            self.passports.append(Passport(entry, validation_requirements))

    def count_valid(self):
        count = 0
        for passport in self.passports:
            if passport.is_valid():
                count += 1

        return count

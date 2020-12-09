from util import load_and_parse
import time

def parse_function(line):
    pass



def convert_to_dict(data):
    rule_dict = {}
    can_be_in = {}
    for rule in data:
        rule = rule.split(" contain ")
        container, contained = rule
        if container[-1] == "s":
            container = container[:-1]
        # print(contained)
        temp = contained.split(", ")
        contained = {}
        for entry in temp:
            num = entry[0]
            entry = entry[2:].strip()
            if "." in entry:
                entry = entry[:-1]

            if entry[-1] == "s":
                entry = entry[:-1]

            if num == "n":
                contained = {"no other bag": 0}
            else:
                contained[entry] = int(num)

        if container in rule_dict:
            rule_dict[container].append(contained)
        else:
            rule_dict[container] = contained

        for key in contained:
            if key in can_be_in:
                can_be_in[key].add(container)
            else:
                can_be_in[key] = set([container])

    return rule_dict, can_be_in


def part_one(data):
    queue = ["shiny gold bag"]
    fits = set()
    found = {"no other bag"}
    while len(queue) > 0:
        cur_bag = queue.pop(0)
        if cur_bag != "shiny gold bag":
            fits.add(cur_bag)
        found.add(cur_bag)
        if cur_bag in data:
            containers = list(data[cur_bag])
        else:
            containers = []
        for container in containers:
            if container not in found and container not in queue:
                queue.append(container)

    return len(fits)

def find_number_needed_for_bag(data, bag_type, memo=None):
    if memo is None:
        memo = {"no other bag": 0}

    if bag_type in memo:
        return memo[bag_type]

    memo[bag_type] = 0
    for contained in data[bag_type]:
        memo[bag_type] +=(1 + find_number_needed_for_bag(data, contained, memo)) * data[bag_type][contained]

    print(bag_type, memo[bag_type])
    return memo[bag_type]

def part_two(data):
    bag_count = 0
    memo = {}
    return find_number_needed_for_bag(data, "shiny gold bag")



# for key in rules:
#     print(f"{key}: {rules[key]}")
# print(rules["wavy plum bag"])
start = time.perf_counter()
data = load_and_parse("data.txt")
rules, fits_in = convert_to_dict(data)
print(part_one(fits_in))
print(find_number_needed_for_bag(rules, "shiny gold bag"))
print(time.perf_counter() - start)
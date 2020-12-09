from util import load_and_parse
from Computer import Computer


def parse_function(line):
    line = line.split(" ")
    line[1] = int(line[1])
    return tuple(line)

data = load_and_parse("data.txt", parse_function)

def run_program(data):
    func_dict = {"acc":add_to_acc, "jmp":jump, "nop": nothing}
    registers = [0,0,0]
    visited = set()
    while 0 <= registers[1] < len(data) and registers[1] not in visited:
        inst, val = data[registers[1]]
        # print(inst, val)
        visited.add(registers[1])
        registers[0] = data[registers[1]][1]
        func_dict[data[registers[1]][0]](registers)


    if registers[1] >= len(data):
        return registers[2]
    else:
        return False

def add_to_acc(args):
    args[2] += args[0]
    args[1] += 1

def jump(args):
    args[1] += args[0]

def nothing(args):
    args[1] += 1

def find_idxs(data):
    idxes = []
    for idx, val in enumerate(data):
        if val[0] in ["nop", "jmp"]:
            idxes.append(idx)

    return idxes

def part_two(data):
    # print(find_idxs(data)[::-1])
    for idx in find_idxs(data)[::-1]:
        cur_data = list(data)
        if cur_data[idx][0] == "nop":
            cur_data[idx] = ("jmp", cur_data[idx][1])
        else:
            cur_data[idx] = ("nop", cur_data[idx][1])

        comp = Computer(cur_data)
        res = comp.run_program()
        if res:
            print(idx)
            return res

    return False
comp = Computer(data)
comp.run_program()
print(comp.get_acc())

def make_graph(data):
    graph = {}
    for idx, value in enumerate(data):
        if value[0] == "jmp":
            graph[idx] = idx + value[1]
        else:
            graph[idx] = idx + 1

    reverse_graph = {}
    for key, value in graph.items():
        if value in reverse_graph:
            reverse_graph[value].append(key)
        else:
            reverse_graph[value] = [key]

    return graph, reverse_graph

graph, rev = make_graph(data)

target_indicies = {}
cur = len(data)
endpoints = rev[cur]
while len(endpoints) > 0:
    if cur in rev:
        endpoints.extend(rev[cur])
    cur = endpoints.pop(0)
    if cur not in target_indicies:
        target_indicies[cur] = True

for value in rev.values():
    for cur in value:
        if cur >= len(data):
            endpoints.append(cur)

for endpoint in endpoints:
    while endpoint in rev:
        if endpoint not in target_indicies:
            target_indicies[endpoint] = True
            endpoint = rev[endpoint]
        else:
            break

cur = graph[0]
def exits_deadlock(val, data, targets):
    op, num = data[val]
    return (op == "jmp" and val + 1 in targets) or (op == "nop" and val + data[val][1] in targets)

while not exits_deadlock(cur, data, target_indicies):
    cur = graph[cur]

data[cur] = ("jmp" if data[cur][0] == "nop" else "nop", data[cur][1])
print(run_program(data))





# print(data[226])
# print(part_two(data))
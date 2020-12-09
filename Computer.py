class Computer:
    def __init__(self, instruction_list):
        self._op_list = instruction_list
        self._memory = [0]
        self._acc = 0
        self._mem_ptr = 0
        self._op_ptr = 0
        self._op_dict = {"nop": self.do_nothing, "jmp": self.jump, "acc":self.add_to_acc}

    def run_program(self):
        visited = set()
        while self._op_ptr not in visited and self._op_ptr < len(self._op_list):
            visited.add(self._op_ptr)
            op_code, val = self._op_list[self._op_ptr]
            self._op_dict[op_code](val)

        if self._op_ptr >= len(self._op_list):
            return self._acc
        else:
            return False

    def do_nothing(self, val):
        self._op_ptr += 1

    def jump(self, val):
        self._op_ptr += val

    def add_to_acc(self, val):
        self._acc += val
        self._op_ptr += 1

    def get_acc(self):
        return self._acc

    def set_acc(self, val):
        self._acc = val

    def load_instructions(self, instruction_list):
        self._op_list = instruction_list

def assembler_parser(line):
    line = line.split(" ")
    line[1] = int(line[1])
    return tuple(line)
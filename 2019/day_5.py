def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data
    
class IntCodeComputer:
    def __init__(self, memory):
        self.memory = memory
        self.pointer = 0
        self.halt = False
        self.output_log = []

        self.opcodes = {
            "01":self.opcode_01,
            "02":self.opcode_02,
            "03":self.opcode_03,
            "04":self.opcode_04,
            "05":self.opcode_05,
            "06":self.opcode_06,
            "07":self.opcode_07,
            "08":self.opcode_08,
            "99":self.opcode_99
        }

    def run(self):
        while not self.halt:
            opcode = self.parse_opcode()
            self.opcodes[opcode]()

    def parse_opcode(self):
        opcode = self.read_val()
        opcode = str(opcode).zfill(5)[-2:]
        return opcode
    
    def parse_modes(self, arg_num=0):
        modes = str(self.read_val())[:-2].zfill(arg_num)[::-1]
        modes = [int(x) for x in modes]
        return modes

    def read_val(self, offset=0, mode=0):
        if mode == 0:
            return self.memory[self.pointer + offset]
        else:
            return self.pointer + offset

    def output(self, val):
        self.output_log.append(val)
        print("OUTPUT: ", val)

    def output_memory(self):
        print(self.memory)

    def input(self):
        return input("INPUT: ")

    def opcode_01(self):
        modes = self.parse_modes(3)
        loc_1 = self.read_val(1, modes[0])
        loc_2 = self.read_val(2, modes[1])
        result = self.read_val(3)
        self.memory[result] = self.memory[loc_1] + self.memory[loc_2]
        self.pointer += 4

    def opcode_02(self):
        modes = self.parse_modes(3)
        loc_1 = self.read_val(1, modes[0])
        loc_2 = self.read_val(2, modes[1])
        result = self.read_val(3)
        self.memory[result] = self.memory[loc_1] * self.memory[loc_2]
        self.pointer += 4

    def opcode_03(self):
        loc = self.read_val(1, 0)
        self.memory[loc] = int(self.input())
        self.pointer += 2

    def opcode_04(self):
        modes = self.parse_modes(1)
        loc = self.read_val(1, modes[0])
        self.output(self.memory[loc])
        self.pointer += 2

    def opcode_05(self):
        modes = self.parse_modes(2)
        val_1 = self.read_val(1, modes[0])
        val_2 = self.read_val(2, modes[1])
        if self.memory[val_1] != 0:
            self.pointer = self.memory[val_2]
        else:
            self.pointer += 3

    def opcode_06(self):
        modes = self.parse_modes(2)
        val_1 = self.read_val(1, modes[0])
        val_2 = self.read_val(2, modes[1])
        if self.memory[val_1] == 0:
            self.pointer = self.memory[val_2]
        else:
            self.pointer += 3

    def opcode_07(self):
        modes = self.parse_modes(3)
        loc_1 = self.read_val(1, modes[0])
        loc_2 = self.read_val(2, modes[1])
        result = self.read_val(3)
        if self.memory[loc_1] < self.memory[loc_2]:
            self.memory[result] = 1
        else:
            self.memory[result] = 0
        self.pointer += 4

    def opcode_08(self):
        modes = self.parse_modes(3)
        loc_1 = self.read_val(1, modes[0])
        loc_2 = self.read_val(2, modes[1])
        result = self.read_val(3)
        if self.memory[loc_1] == self.memory[loc_2]:
            self.memory[result] = 1
        else:
            self.memory[result] = 0
        self.pointer += 4

    def opcode_99(self):
        self.halt = True

def first_star(data):
    comp = IntCodeComputer(data)
    comp.run()
    output = comp.output_log
    return output[-1]

def second_star(data):
    comp = IntCodeComputer(data)
    comp.run()
    output = comp.output_log
    return output[-1]

def solution(source):
    data = load_input(source)
    data = [int(x) for x in data.split(",")]
    print("Day 5")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

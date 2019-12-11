# This class is used in many of the puzzle solutions, with slight changes as it evolves.
# This file contains the completed version, used by solutions which merely use the computer, rather than evolve it. Intermediate
# versions of the computer are stored in their respective solution files.


class IntCodeComputer:
    def __init__(self, memory, input_list=[]):
        self.memory = memory
        self.memory.extend([0 for x in range(10000)])
        self.pointer = 0
        self.relative_base = 0
        self.halt = False
        self.pause = False
        self.output_log = []
        self.input_list = input_list

        self.opcodes = {
            "01": self.opcode_01,
            "02": self.opcode_02,
            "03": self.opcode_03,
            "04": self.opcode_04,
            "05": self.opcode_05,
            "06": self.opcode_06,
            "07": self.opcode_07,
            "08": self.opcode_08,
            "09": self.opcode_09,
            "99": self.opcode_99
        }

    def run(self):
        while not (self.halt or self.pause):
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
        elif mode == 1:
            return self.pointer + offset
        elif mode == 2:
            return self.relative_base + self.memory[self.pointer + offset]

    def output(self, val):
        self.output_log.append(val)

    def output_memory(self):
        print(self.memory)

    def add_input(self, value):
        self.input_list.append(value)
        if self.pause:
            self.pause = False

    def read_input(self):
        if len(self.input_list) > 0:
            return int(self.input_list.pop(0))
        else:
            return None

    def opcode_01(self):
        modes = self.parse_modes(3)
        loc_1 = self.read_val(1, modes[0])
        loc_2 = self.read_val(2, modes[1])
        result = self.read_val(3, modes[2])
        self.memory[result] = self.memory[loc_1] + self.memory[loc_2]
        self.pointer += 4

    def opcode_02(self):
        modes = self.parse_modes(3)
        loc_1 = self.read_val(1, modes[0])
        loc_2 = self.read_val(2, modes[1])
        result = self.read_val(3, modes[2])
        self.memory[result] = self.memory[loc_1] * self.memory[loc_2]
        self.pointer += 4

    def opcode_03(self):
        modes = self.parse_modes(1)
        loc = self.read_val(1, modes[0])
        val = self.read_input()
        if val != None:
            self.memory[loc] = val
            self.pointer += 2
        else:
            self.pause = True

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
        result = self.read_val(3, modes[2])
        if self.memory[loc_1] < self.memory[loc_2]:
            self.memory[result] = 1
        else:
            self.memory[result] = 0
        self.pointer += 4

    def opcode_08(self):
        modes = self.parse_modes(3)
        loc_1 = self.read_val(1, modes[0])
        loc_2 = self.read_val(2, modes[1])
        result = self.read_val(3, modes[2])
        if self.memory[loc_1] == self.memory[loc_2]:
            self.memory[result] = 1
        else:
            self.memory[result] = 0
        self.pointer += 4

    def opcode_09(self):
        modes = self.parse_modes(1)
        loc = self.read_val(1, modes[0])
        self.relative_base += self.memory[loc]
        self.pointer += 2

    def opcode_99(self):
        self.halt = True

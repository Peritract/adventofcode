import operator

operations = {
        "PUSH": lambda x: x,
        "AND": operator.and_,
        "OR": operator.or_,
        "NOT": operator.invert,
        "LSHIFT": operator.lshift,
        "RSHIFT": operator.rshift
    }

def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line)
    if len(data) == 1:
        data = data[0]
    return data

class Wire:
    def __init__(self,operation,wires_in):
        self.op = operation
        self.inp = wires_in
        self.val = None

    def get_out(self):
        if self.val != None:
            return self.val #If the value has been worked out before, return it
        else:
            #Otherwise, work out the value now, by asking the input wires for their values, and performing the operation on the response. Recursion happens here. 
            self.val = operations[self.op](*[int(x) if x.isdigit() else wires[x].get_out() for x in self.inp])
            return self.val
            

def parse_instruction(line):
    process, output = line.split(" -> ")
    process = process.split(" ")
    if len(process) == 1:
        op = "PUSH"
        data = [process[0]] #Always pass a list, so that * unpacking arguments works later.
    elif process[0] == "NOT":
        op = "NOT"
        data = [process[1]]
    else:
        op = process[1]
        data = [process[0],process[2]]
    return output, Wire(op, data)

def parse_input(data):
    for line in data:
       wire, n = parse_instruction(line.strip())
       wires[wire] = n

def first_star():
    return wires["a"].get_out()

    
def second_star():
    a = wires["a"].get_out()
    for x in dict.keys(wires):
        wires[x].val = None
    wires["b"].val = a
    return wires["a"].get_out()

wires = {}

def solution(source):
    parse_input(load_input(source))
    print("Day 7")
    print("First star:", str(first_star()))
    print("Second star:", str(second_star()))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data
    
def get_val(data, pointer):
    return data[pointer]

def int_code_computer(data):
    pointer = 0
    while data[pointer] != 99:
        if data[pointer] == 1:
            data[get_val(data, pointer + 3)] = data[get_val(data, pointer + 1)] + data[get_val(data, pointer + 2)]
            pointer += 4
        elif data[pointer] == 2:
            data[get_val(data, pointer + 3)] = data[get_val(data, pointer + 1)] * data[get_val(data, pointer + 2)]
            pointer += 4
    return data[0]

def first_star(data):
    data[1], data[2] = 12,2
    return int_code_computer(data)


def second_star(data):
    for noun in range(0, 100):
        for verb in range(0, 100):
            test_data = data.copy()
            test_data[1], test_data[2] = noun, verb
            if int_code_computer(test_data) == 19690720:
                return 100 * noun + verb

def solution(source):
    data = load_input(source)
    data = [int(x) for x in data.split(",")]
    print("Day 2")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

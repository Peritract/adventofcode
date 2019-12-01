import math

def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data
    
def calculate_module_fuel(mass):
    return math.floor(mass / 3) - 2

def recursively_calculate_module_fuel(mass):
    fuel = calculate_module_fuel(mass)
    if fuel <= 0:
        return 0
    else:
        return  fuel + recursively_calculate_module_fuel(fuel)

def first_star(data):
    total = 0
    for i in data:
        total += calculate_module_fuel(int(i))
    return total

def second_star(data):
    total = 0
    for i in data:
        total += recursively_calculate_module_fuel(int(i))
    return total

def solution(source):
    data = load_input(source)
    print("Day N")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

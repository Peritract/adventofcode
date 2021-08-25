def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line)
    if len(data) == 1:
        data = data[0]
    return data
    

def first_star(data):
    floor = 0
    for i in data:
        if i ==")":
            floor -= 1
        elif i == "(":
            floor += 1
    return floor

def second_star(data):
    floor = 0
    for i in range(0, len(data)):
        if data[i] ==")":
            floor -= 1
        elif data[i] == "(":
            floor += 1
        if floor < 0:
            return i + 1
    return "invalid input"

def solution(source):
    data = load_input(source)
    print("Day 1")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")
    

if __name__ == "__main__":
    solution("input.txt")
    

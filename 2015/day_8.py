def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data
    

def first_star(data):
    full = 0
    escaped = 0
    for line in data:
        full += len(line)
        temp = 0
        i= 1 
        while i <= len(line) - 2:
            if line[i] == " ":
                pass
            elif line[i] != "\\":
                temp += 1
            else:
                if line[i + 1] == "\\" or line[i + 1] == '"':
                    temp += 1
                    i += 1
                elif line[i + 1] == "x":
                    temp += 1
                    i += 3
            i += 1
        escaped += temp
    return full - escaped

def second_star(data):
    full = 0
    encoded = 0
    for line in data:
        full += len(line)
        temp = 0
        for i in line:
            if i == '"' or i == "\\":
                temp += 1
            temp += 1
        encoded += temp + 2
    return encoded - full

def solution(source):
    data = load_input(source)
    print("Day 8")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

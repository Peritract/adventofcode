def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line)
    if len(data) == 1:
        data = data[0]
    return data

def parse_input(data):
    return [x.strip() for x in data.split(", ")]

def first_star(data):
    heading = 0
    x = 0
    y = 0
    for line in data:
        if line[0] == "L":
            heading -= 1
            if heading < 0:
                heading = 3
        elif line[0] == "R":
            heading += 1
            if heading > 3:
                heading = 0
        if heading == 0:
            y -= int(line[1:])
        elif heading == 2:
            y += int(line[1:])
        elif heading == 1:
            x += int(line[1:])
        elif heading == 3:
            x -= int(line[1:])
    return abs(x) + abs(y)
        
        

def second_star(data):
    heading = 0
    x = 0
    y = 0
    locations = [(0,0)]
    for line in data:
        if line[0] == "L":
            heading -= 1
            if heading < 0:
                heading = 3
        elif line[0] == "R":
            heading += 1
            if heading > 3:
                heading = 0
        l = int(line[1:])
        if heading == 0:
            for i in range(0, l):
                y -= 1
                if (x,y) in locations:
                    return abs(x) + abs(y)
                else:
                    locations.append((x,y))
        elif heading == 2:
            for i in range(0, l):
                y += 1
                if (x,y) in locations:
                    return abs(x) + abs(y)
                else:
                    locations.append((x,y))
        elif heading == 1:
            for i in range(0, l):
                x += 1
                if (x,y) in locations:
                    return abs(x) + abs(y)
                else:
                    locations.append((x,y))
        elif heading == 3:
            for i in range(0, l):
                x -= 1
                if (x,y) in locations:
                    return abs(x) + abs(y)
                else:
                    locations.append((x,y))

def solution(source):
    data = parse_input(load_input(source))
    print("Day 1")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

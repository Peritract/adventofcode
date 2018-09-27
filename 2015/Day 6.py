def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line)
    if len(data) == 1:
        data = data[0]
    return data

def parse_line(line):
    temp = line.strip().split(" ")
    if temp[0] == "toggle":
        temp[1] = [int(x) for x in temp[1].split(",")]
        temp[3] = [int(x) for x in temp[3].split(",")]
        temp = [temp[0],temp[1],temp[3]]
    else:
        temp[2] = [int(x) for x in temp[2].split(",")]
        temp[4] = [int(x) for x in temp[4].split(",")]
        temp = [temp[1],temp[2],temp[4]]
    return temp

def parse_input(data):
    new_data = []
    for line in data:
        new_data.append(parse_line(line))
    return new_data

def first_star(data):
    lights = [[False for x in range(0,1000)] for y in range(0,1000)]
    for line in data:
        if line[0] == "on":
            for y in range(line[1][1],line[2][1] + 1):
                for x in range(line[1][0],line[2][0] + 1):
                    lights[y][x] = True
        elif line[0] == "off":
            for y in range(line[1][1],line[2][1] + 1):
                for x in range(line[1][0],line[2][0] + 1):
                    lights[y][x] = False
        else:
            for y in range(line[1][1],line[2][1] + 1):
                for x in range(line[1][0],line[2][0] + 1):
                    lights[y][x] = not lights[y][x]
    count = 0
    for y in range(0,1000):
        for x in range(0,1000):
            if lights[y][x] == True:
                count += 1
    return count

def second_star(data):
    lights = [[0 for x in range(0,1000)] for y in range(0,1000)]
    for line in data:
        if line[0] == "on":
            for y in range(line[1][1],line[2][1] + 1):
                for x in range(line[1][0],line[2][0] + 1):
                    lights[y][x] += 1
        elif line[0] == "off":
            for y in range(line[1][1],line[2][1] + 1):
                for x in range(line[1][0],line[2][0] + 1):
                    if lights[y][x] > 0:
                        lights[y][x] -= 1
        else:
            for y in range(line[1][1],line[2][1] + 1):
                for x in range(line[1][0],line[2][0] + 1):
                    lights[y][x] += 2
    count = 0
    for y in range(0,1000):
        for x in range(0,1000):
            count += lights[y][x]
    return count

def solution(source):
    data = parse_input(load_input(source))
    print("Day 6")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

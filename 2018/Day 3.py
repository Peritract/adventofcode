def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data

def parse_shape(line):
    # Cuts a line into measurements.
    line = line.split(" ")
    code = line[0]
    x, y = line[2].split(",")
    y = y[:-1]
    w, h = line[3].split("x")
    return [code, int(x), int(y), int(w), int(h)]

def place_shape(rect, cloth):
    for y in range(rect[2], rect[2] + rect[4]):
        for x in range(rect[1], rect[1] + rect[3]):
            cloth[y][x] += 1

def check_shape(rect, cloth):
    for y in range(rect[2], rect[2] + rect[4]):
        for x in range(rect[1], rect[1] + rect[3]):
            if cloth[y][x] > 1:
                return False
    return True

def first_star(data,cloth):
    count = 0
    for i in data:
        place_shape(parse_shape(i), cloth)
    for y in range(1000):
        for x in range(1000):
            if cloth[y][x] > 1:
                count += 1
    return count
        

def second_star(data, cloth):
    for i in data:
        if check_shape(parse_shape(i), cloth):
            return parse_shape(i)[0]


def solution(source):
    data = load_input(source)
    cloth = [[0 for x in range(1000)] for y in range(1000)]
    print("Day 3")
    print("First star:", str(first_star(data, cloth)))
    print("Second star:", str(second_star(data, cloth)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

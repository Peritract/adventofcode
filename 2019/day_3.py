def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data
    
def trace_wire(path):
    locations = []
    headings = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
    location = (0, 0, 0)
    count = 0
    for step in path.split(","):
        count += 1
        direction = step[0]
        distance = int(step[1:])
        for i in range(distance):
            location = tuple(x + y for x, y in zip(location, headings[direction]))
            locations.append(location)
    return set(locations)

def trace_wire_distances(path):
    locations = []
    headings = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
    location = (0, 0, 0)
    count = 0
    visited={}
    for step in path.split(","):
        direction = step[0]
        distance = int(step[1:])
        for i in range(distance):
            count += 1
            location = tuple(x + y for x, y in zip(location, headings[direction]))
            locations.append(location)
            if location not in visited.keys():
                visited[location] = count
    return set(locations), visited

def first_star(data):
    wire_1 = trace_wire(data[0])
    wire_2 = trace_wire(data[1])
    crosses = wire_1.intersection(wire_2)
    return min(map(lambda x: abs(x[0]) + abs(x[1]), crosses))

def second_star(data):
    wire_1, visited_1 = trace_wire_distances(data[0])
    wire_2, visited_2 = trace_wire_distances(data[1])
    crosses = wire_1.intersection(wire_2)
    return min(map(lambda x: visited_1[x] + visited_2[x], crosses))

def solution(source):
    data = load_input(source)
    print("Day 3")
    print("First star:", first_star(data))
    print("Second star:", second_star(data))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

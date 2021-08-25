from itertools import permutations

def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data

def extract_details(data):
    dists = {}
    places = set()
    for x in data:
        x = x.split()
        dists[(x[0], x[2])] = int(x[4])
        dists[(x[2], x[0])] = int(x[4])
        places.add(x[0])
        places.add(x[2])
    return dists, places

def find_dist(route, dists):
    dist = 0
    for i in range(0, len(route) - 1):
        dist += dists[(route[i], route[i + 1])]
    return dist

def first_star(data):
    dists, places = extract_details(data)
    return min([find_dist(route, dists) for route in permutations(places)])

def second_star(data):
    dists, places = extract_details(data)
    return max([find_dist(route, dists) for route in permutations(places)])


def solution(source):
    data = load_input(source)
    print("Day 9")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
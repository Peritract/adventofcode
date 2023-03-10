def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line)
    if len(data) == 1:
        data = data[0]
    return data
    

def first_star(data):
    location = (0,0)
    visited = [location]
    for move in data:
        if move == "<":
            location = (location[0] -1,location[1])
        elif move == ">":
            location = (location[0] + 1,location[1])
        elif move == "^":
            location = (location[0],location[1] - 1)
        else:
            location = (location[0],location[1] + 1)
        if not location in visited:
            visited.append(location)
    return(len(visited))
    

def second_star(data):
    location = (0,0)
    location_2 = (0,0)
    visited = [location]
    for i in range(0, len(data)):
        move = data[i]
        if i % 2 == 0:
            if move == "<":
                location = (location[0] -1,location[1])
            elif move == ">":
                location = (location[0] + 1,location[1])
            elif move == "^":
                location = (location[0],location[1] - 1)
            else:
                location = (location[0],location[1] + 1)
            if not location in visited:
                visited.append(location)
        else:
            if move == "<":
                location_2 = (location_2[0] -1,location_2[1])
            elif move == ">":
                location_2 = (location_2[0] + 1,location_2[1])
            elif move == "^":
                location_2 = (location_2[0],location_2[1] - 1)
            else:
                location_2 = (location_2[0],location_2[1] + 1)
            if not location_2 in visited:
                visited.append(location_2)
    return(len(visited))

def solution(source):
    data = load_input(source)
    print("Day 3")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

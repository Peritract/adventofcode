import math

def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data

def get_asteroids(data):
    asteroids = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "#":
                asteroids[(x, y)] = 0
    return asteroids

def get_angles(asteroids, start_x, start_y):
    angles = {}
    for asteroid in asteroids.keys():
        if asteroid != (start_x, start_y):
            x = asteroid[0]
            y = asteroid[1]
            angle = math.atan2(start_x - x, start_y - y)
            angles[(x, y)] = angle
    return angles

def get_asteroids_for_angles(angles):
    angle_dict = {}
    for k, v in angles.items():
        if v in angle_dict:
            angle_dict[v].append(k)
        else:
            angle_dict[v] = [k]
    return angle_dict

def count_visible(asteroids, start_x, start_y):
    angles = get_angles(asteroids, start_x, start_y)
    return len(set(angles.values()))

def find_closest(targets, site):
    dists = [abs(x[0] - site[0]) + abs(x[1] - site[1]) for x in targets]
    return dists.index(min(dists))

def first_star(data):
    asteroids = get_asteroids(data)
    visible = {}
    for asteroid in asteroids.keys():
        visible[asteroid] = count_visible(asteroids, asteroid[0], asteroid[1])
    max_seen = max(visible.values())
    best_place = [key for key in visible.keys() if visible[key] == max_seen][0]
    return f"{best_place}: {max_seen}"

def second_star(data):
    origin = (23,19)
    asteroids = get_asteroids(data)
    angles = get_angles(asteroids, origin[0], origin[1])
    angle_dict = get_asteroids_for_angles(angles)
    
    all_angles =  sorted(list(angle_dict.keys()))
    
    start = all_angles.index(0.0)
    count = 0
    while any([True for x in angle_dict.keys() if angle_dict[x] != []]):
        index = all_angles[start]
        if angle_dict[index] != []:
            target_index = find_closest(angle_dict[index], origin)
            zapped = angle_dict[index].pop(target_index)
            count += 1
            if count == 200:
                return zapped[0] * 100 + zapped[1]
        start -= 1
        if start < 0:
            start = len(all_angles) - 1




def solution(source):
    data = load_input(source)
    print("Day 10")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

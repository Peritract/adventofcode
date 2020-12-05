def load_input(source="input.txt"):
    with open(source, 'r') as file:
        return [x.strip() for x in file.readlines()]

def partition(rng, down=True):
    if type(rng) == int:
        return rng
    elif len(rng) == 2:
        return rng[0] if down else rng[1]
    mid = len(rng) // 2
    if down:
        return rng[:mid]
    else:
        return rng[mid:]
    
def find_loc(seat, down='F', limit=127):
    loc = [y for y in range(limit + 1)]
    for x in seat:
        if x == down:
            loc = partition(loc)
        else:
            loc = partition(loc, False)
    return loc
    
def first_star(data):
    for seat in data:
        r = find_loc(seat[:7])
        s = find_loc(seat[7:], 'L', 7)
        seat_id = r * 8 + s
        ids.append(seat_id)
    
    return max(ids)

def second_star(data):
    for seat in data:
            r = find_loc(seat[:7])
            s = find_loc(seat[7:], 'L', 7)
            seat_id = r * 8 + s
            ids.append(seat_id)
    
    for x in range(max(ids) + 1):
        if x > 100 and x not in ids:
            return x
    
def solution(source):
    data = load_input(source)
    print("Day 5")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

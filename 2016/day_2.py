def load_input(source="input.txt"):
    with open(source, 'r') as file:
        return [x.strip() for x in file.readlines()]
    
def first_star(data):
    nums = []
    pad = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    loc = [1, 1]
    for line in data:
        for x in line:
            if x == 'U' and loc[1] > 0:
                loc[1] -= 1
            elif x == 'D' and loc[1] < 2:
                loc[1] += 1
            elif x == 'L' and loc[0] > 0:
                loc[0] -= 1
            elif x == 'R' and loc[0] < 2:
                loc[0] += 1
        nums.append(pad[loc[1]][loc[0]])
    
    return "".join([str(x) for x in nums])

def is_valid(x, y, pad):
    if not(0 <= x < len(pad) and 0 <= y < len(pad)):
        return False
    elif pad[y][x] != 'X':
        return True
    return False

def second_star(data):
    nums = []
    pad = ["XX1XX", "X234X", "56789", "XABCX", "XX9XX"]
    loc = [0, 2]
    
    for line in data:
        for x in line:
            if x == 'U' and is_valid(loc[0], loc[1] - 1, pad):
                loc[1] -= 1
            elif x == 'D' and is_valid(loc[0], loc[1] + 1, pad):
                loc[1] += 1
            elif x == 'L' and is_valid(loc[0] - 1, loc[1], pad):
                loc[0] -= 1
            elif x == 'R' and is_valid(loc[0] + 1, loc[1], pad):
                loc[0] += 1
        nums.append(pad[loc[1]][loc[0]])
    
    return "".join([x for x in nums])
    
def solution(source):
    data = load_input(source)
    print("Day 12")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

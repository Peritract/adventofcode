def load_input(source):
    with open(source) as f:
        data = [[int(y) for y in x.strip().split()] for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data

def is_safe(r):
    diffs = [r[i] - r[i + 1] for i in range(len(r) - 1)]
    return (all(x > 0 for x in diffs) or all(x < 0 for x in diffs)) and all(1 <= abs(x) <=3 for x in diffs)

def first_star(data):
    valid = 0
    for r in data:
        valid += is_safe(r)
    return valid


def second_star(data):
    valid = 0
    for r in data:
        if is_safe(r):
            valid += 1
        else:
            v = False 
            for i in range(len(r)):
                s = r[:]
                s.pop(i)
                if is_safe(s):
                    v = True
            valid += v
    return valid
        
    
def solution(source):
    data = load_input(source)
    print("Day 2")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

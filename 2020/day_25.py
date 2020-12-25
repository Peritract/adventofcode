def load_input(source="input.txt"):
    with open(source, 'r') as file:
        return [int(x) for x in file.readlines()]

def find_loop_size(num, subj=7):
    val = 1
    loop = 0
    while val != num:
        val = val * 7
        val = val % 20201227
        loop += 1
    return loop

def transform_key(loop_size, subj):
    loops = 0
    val = 1
    while loops < loop_size:
        val = val * subj
        val = val % 20201227
        loops += 1
    return val

def first_star(data):
    card = find_loop_size(data[0])
    door = find_loop_size(data[1])
    
    return (transform_key(card, data[1]), transform_key(door, data[0]))
    
def second_star(data, turns=100):
    pass
    
def solution(source):
    data = load_input(source)
    print("Day 25")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

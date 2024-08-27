def load_input(source):
    with open(source) as f:
        return int(f.read().strip())

def first_star(num):
    layer = 1
    max_val = 1
    min_val = 0
    while max_val < num:
        layer += 1
        if layer % 2:
            min_val = max_val + 1
            max_val = layer ** 2
    layer_steps = layer // 2 + 1
    mids = [max_val - layer // 2]
    for i in range(3):
        mids.append(mids[-1] - (layer - 1))
        
    return layer_steps + min(abs(x - num) for x in mids) - 1


def second_star(data):
    return None


def solution(source):
    data = load_input(source)
    print("Day 2")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

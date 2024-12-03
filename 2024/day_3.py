import re

def load_input(source):
    with open(source) as f:
        data = f.read()
    if len(data) == 1:
        data = data[0]
    return data

def first_star(data):
    muls = re.findall(r"(mul\(\d+,\d+\))", data)
    tot = 0
    for m in muls:
        nums = [int(x) for x in re.findall(r"(\d+)", m)]
        tot += nums[0] * nums[1]
    return tot

def second_star(data):
    segs = re.split(r"(do(?:n't)?\(\))", data)
    tot = 0
    enabled = True
    for s in segs:
        if s == "do()":
            enabled = True
        elif s == "don't()":
            enabled = False
        elif enabled:
            muls = re.findall(r"(mul\(\d+,\d+\))",s)
            for m in muls:
                nums = [int(x) for x in re.findall(r"(\d+)", m)]
                tot += nums[0] * nums[1]
    return tot
    
def solution(source):
    data = load_input(source)
    print("Day 3")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

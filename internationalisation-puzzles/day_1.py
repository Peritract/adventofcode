def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data
    
def answer(data):
    total = 0
    for row in data:
        b_l = len(row.encode())
        s_l = len(row)
        if s_l <= 140 and b_l <= 160:
            total += 13
        elif b_l <= 160:
            total += 11
        elif s_l <= 140:
            total += 7
    return total

def solution(source):
    data = load_input(source)
    print("Day 1")
    print("Answer:", str(answer(data)))


if __name__ == "__main__":
    solution("input.txt")

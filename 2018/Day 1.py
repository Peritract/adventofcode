def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line)
    if len(data) == 1:
        data = data[0]
    return data
    

def first_star(data):
    freq = 0
    for i in data:
        freq += int(i)
    return freq

def second_star(data):
    freq = 0
    freqs = {0: 1}
    while True:
        for i in data:
            freq += int(i)
            if freq in freqs:
                return freq
            else:
                freqs[freq] = 1

def solution(source):
    data = load_input(source)
    print("Day 1")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

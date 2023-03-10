def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data
    
def parse(text):
    res = ""
    curr = text[0]
    for i in range(1, len(text)):
        if curr[-1] != text[i]:
            res += str(len(curr)) + curr[-1]
            curr = text[i]
        else:
            curr += text[i]
    res += str(len(curr)) + curr[-1]
    return res



def first_star(data):
    text = data
    for i in range(50):
        text = parse(text)
    return len(text)

def second_star(data):
    return "Not solved"

def solution(source):
    data = load_input(source)
    print("Day 10")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
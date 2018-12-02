def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data
    

def first_star(data):
    return "Not solved"

def second_star(data):
    return "Not solved"

def solution(source):
    data = load_input(source)
    print("Day N")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

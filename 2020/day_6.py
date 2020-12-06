def load_input(source="input.txt"):
    with open(source, 'r') as file:
        return [x.strip() for x in file.read().split('\n\n')]
    
def first_star(data):
    return sum([len(set(x.replace('\n', ''))) for x in data])


def second_star(data):
    groups  = [[set(y) for y in x.split('\n')] for x in data]
    questions = [len(x[0].intersection(*x[1:])) for x in groups]
    return sum(questions)
    
def solution(source):
    data = load_input(source)
    print("Day 6")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

import re

def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data

def parse_aunt(text):
    data = {
        "key": int(re.match("^Sue (\d+):", text).group(1))
    }
    for m in re.findall("([a-z]+): (\d+)", text):
        data[m[0]] = int(m[1])
    return data
    
rules = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

def find_aunt(aunts):
    for aunt in aunts:
        if all([k not in rules or rules[k] == v for k, v in aunt.items()]):
            return aunt["key"]
        
def find_complex_aunt(aunts):
    for aunt in aunts:
        matches = []
        for k, v in aunt.items():
            if k in rules:
                if k in ('cats', 'trees'):
                    matches.append(rules[k] < v)
                elif k in ('pomeranians', 'goldfish'):
                    matches.append(rules[k] > v)
                else:
                    matches.append(rules[k] == v)
        if all(matches):
            return aunt["key"]

def first_star(data):
    aunts = [parse_aunt(a) for a in data]
    return find_aunt(aunts)


def second_star(data):
    aunts = [parse_aunt(a) for a in data]
    return find_complex_aunt(aunts)

def solution(source):
    data = load_input(source)
    print("Day 16")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

import re

def load_input(source="input.txt"):
    with open(source, 'r') as file:
        text = file.read()
    blocks = text.split("\n\n")
    rules = [re.findall("(^[a-z\s]+|\d+-\d+)", x) for x in blocks[0].split("\n")]
    rules = {x[0]:[tuple([int(z) for z in y.split("-")]) for y in x[1:]] for x in rules}
    mine = [int(x) for x in blocks[1].split("\n")[1].split(",")]
    tickets = [[int(x) for x in y.split(",")] for y in blocks[2].split("\n")[1:]]
    return {"rules": rules,
            "mine": mine,
            "tickets": tickets}

def find_valid_values(rules):
    valid = set()
    for rule in rules.values():
        for x in rule:
            for y in range(x[0], x[1] + 1):
                valid.add(y)
    return valid
    
def first_star(data):
    valid = find_valid_values(data["rules"])
    invalid = 0
    for ticket in data["tickets"]:
        for value in ticket:
            if value not in valid:
                invalid += value
    return invalid

def is_valid(rule, col):
    valid = True
    for val in col:
        if not rule[0][0] <= val <= rule[0][1] and not rule[1][0] <= val <= rule[1][1]:
            return False
    return True

def determine_fields(possibles):
    changes = True
    final = {}
    to_remove = []
    while changes == True:
        changes = False
        for rule in possibles:
            if possibles[rule] != None:
                opts = possibles[rule]
                for opt in opts:
                    if opt in to_remove:
                        opts.remove(opt)
                        changes = True
                if len(opts) == 1:
                    val = opts[0]
                    final[rule] = val
                    to_remove.append(val)
                    possibles[rule] = None
                    changes = True
                else:
                    possibles[rule] = opts
    return final    
    
def second_star(data):
    
    # Only keep valid tickets
    valid = find_valid_values(data["rules"])
    tickets = [x for x in data["tickets"] if all([y in valid for y in x])]
    # Identify rules somehow
    possibles = {}
    for rule in data["rules"]:
        valids = []
        for i in range(len(tickets[0])):
            col = [x[i] for x in tickets]
            if is_valid(data["rules"][rule], col):
                valids.append(i)
        possibles[rule] = valids
    rules = determine_fields(possibles)
    num = 1
    for x in rules:
        if x.startswith("departure"):
            num *= data["mine"][rules[x]]
    return num
    
def solution(source):
    data = load_input(source)
    print("Day 16")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

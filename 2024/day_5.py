from collections import defaultdict

def load_input(source):
    with open(source) as f:
        data = f.read()
    return data


def format_rules(rules):
    before = defaultdict(lambda: [])
    for r in rules:
        before[r[1]].append(r[0])
    return before


def parse_input(data):
    rules, updates = data.split("\n\n")
    rules = format_rules([[int(x) for x in r.split("|")] for r in rules.split()])
    updates = [[int(x) for x in u.split(",")] for u in updates.split()]

    return rules, updates


def is_valid_update(rules, update):
    for i, v in enumerate(update):
        before = rules[v]
        for x in before:
            if x in update and not update.index(x) < i:
                return False
    return True


def first_star(data):
    rules, updates = data
    valid_middles = []
    for u in updates:
        if is_valid_update(rules, u):
            valid_middles.append(u[int(len(u) / 2)])
    return sum(valid_middles)


def reorder_update(rules, update):
    relevant_rules = {v:[x for x in rules[v] if x in update] for v in update}
    rule_counts = {k:len(v) for k,v in relevant_rules.items()}
    correct = []
    while len(correct) < len(update):
        v = min(rule_counts, key=rule_counts.get)
        del rule_counts[v]
        correct.append(v)
    
    return correct


def second_star(data):
    rules, updates = data
    invalid_middles = []
    for u in updates:
        if not is_valid_update(rules, u):
            u = reorder_update(rules, u)
            invalid_middles.append(u[int(len(u) / 2)])
    return sum(invalid_middles)
    
def solution(source):
    data = parse_input(load_input(source))
    print("Day 5")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

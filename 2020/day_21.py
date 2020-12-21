from collections import defaultdict

def load_input(source="input.txt"):
    foods = defaultdict(lambda: [])
    foods['ingredients'] = set()
    with open(source, 'r') as file:
        data = file.readlines()
        for line in data:
            ing, alg = line.split('(contains')
            ing = ing.strip().split(' ')
            alg = alg.strip()[:-1].split(', ')
            for a in alg:
                foods[a].append(set(ing))
            foods['ingredients'].update(ing)
            foods['recipes'].extend(ing)
    return foods

def first_star(data):
    seen = set()
    for alg in data:
        if alg not in ('ingredients', 'recipes'):
            rec = data[alg]
            narrow = rec[0].intersection(*rec[1:])
            seen.update(narrow)
    safe = data['ingredients'] - seen
    count = 0
    for x in safe:
        count += data['recipes'].count(x)
    return count
        
def second_star(data):
    for alg in data:
        if alg not in ('ingredients', 'recipes'):
            rec = data[alg]
            data[alg] = rec[0].intersection(*rec[1:])
    del data['ingredients']
    del data['recipes']
    
    final = {}
    
    while len(final) != len(data):
        for k,v in data.items():
            if len(v) == 1:
                final[k] = v
                for k,v2 in data.items():
                    data[k] = v2 - v
    sortable = list(final.items())
    
    return ",".join([list(x[1])[0] for x in sorted(sortable, key=lambda a: a[0])])
    
def solution(source):
    data = load_input(source)
    print("Day 21")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

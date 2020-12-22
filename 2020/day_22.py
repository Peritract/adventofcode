# I neede a hint for this one, because I did not read the question properly; that's on me.

import re
from copy import deepcopy

def load_input(source="input.txt"):
    data = {}
    with open(source, 'r') as file:
        text = file.read()
    chunks = text.split('\n\n')
    for chunk in chunks:
        data[int(re.search('\d+', chunk).group())] = [int(x) for x in chunk.split('\n')[1:]]
    
    return data
    
def first_star(data):
    while len(data[1]) > 0 and len(data[2]) > 0:
        a = data[1].pop(0)
        b = data[2].pop(0)
        if a > b:
            data[1].extend([a, b])
        else:
            data[2].extend([b, a])
    
    scores = [score(val) for val in data.values()]
    return max(scores)

def score(arr):
    return sum([x * (i + 1) for i, x in enumerate(reversed(arr))])

def recursive_combat(data):
    seen = set()
    
    while len(data[1]) > 0 and len(data[2]) > 0:
        
        deck_string = " ".join([str(x) for x in data[1]]) + ' | ' + " ".join([str(x) for x in data[2]])
        
        if deck_string in seen:
            return (1, score(data[1]))
        else:
            seen.add(deck_string)
    
        a = data[1].pop(0)
        b = data[2].pop(0)
        
        if a <= len(data[1]) and b <= len(data[2]):
            new_data = {1 : deepcopy(data[1][:a]), 2: deepcopy(data[2][:b])}
            
            subgame = recursive_combat(new_data)
            
            if subgame[0] == 1:
                data[1].extend([a, b])
            else:
                data[2].extend([b, a])
        else:
            if a > b:
                data[1].extend([a, b])
            else:
                data[2].extend([b, a])
    
    scores = [score(data[x]) for x in range(1, 3)]
    return (1 if scores[0] > scores[1] else 2, max(scores))    
        
def second_star(data):
    result = recursive_combat(data)
    return result[1]
    
def solution(source):
    data = load_input(source)
    print("Day 22")
    print("First star:", str(first_star(deepcopy(data))))
    print("Second star:", str(second_star(deepcopy(data))))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

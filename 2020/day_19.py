import re
import regex as rg

def load_input(source="input.txt"):
    with open(source, 'r') as file:
        text = file.read()
        
    blocks = text.split('\n\n')

    rules = {int(x.split(':')[0]):x.split(':')[1].strip() for x in blocks[0].split('\n')}
    
    for k, v in rules.items():
        if re.match('"[a-z]"', v):
            rules[k] = v[1]
   
    data = {'messages': [x for x in blocks[1].split('\n')],
            'rules': rules}
    
    return data

def is_simple(rule):
    if len(rule) == 1:
        return True
    elif not re.search('\d', rule):
        return True

def collapse(rule):
    if not is_simple(rule):
        return rule
    else:
        spaceless = "".join(rule.split(" "))
        if rule.count('|') > 0:
            return f"({spaceless})"
        else:
            return spaceless

def make_replacements(rule, replacers):
    text = rule
    for k, v in replacers.items():
        rgx = r'\b' + str(k) + r'\b'
        text = re.sub(rgx, v, text)
    return text

def simplify_rules(r):
    rules = r.copy()
    replacers = {k:collapse(v) for k, v in rules.items() if is_simple(v)}
    while len(replacers.keys()) != len(rules.keys()):
        replacers = {k:collapse(v) for k, v in rules.items() if is_simple(v)}
        for k, v in rules.items():
            if k not in replacers:
                n_v = make_replacements(v, replacers)
                if is_simple(n_v):
                    rules[k] = collapse(n_v)
                else:
                    rules[k] = n_v
    return replacers
        
def first_star(data):
    rules = simplify_rules(data['rules'])
    check = rules[0]
    pat = r'^' + check + r'$'
    valid = 0
    for msg in data['messages']:
        if rg.match(pat, msg):
            valid += 1
    return valid
    
def second_star(data):
    rules = data['rules']
    rules[8] = "( ( 42 ) + )"
    rules[11] = "(?P<ft> 42 (?&ft)? 31)"
    rules = simplify_rules(rules)
    check = rules[0]
    pat = r'^' + check + r'$'
    valid = 0
    for msg in data['messages']:
        if rg.match(pat, msg):
            valid += 1
    return valid
    
def solution(source):
    data = load_input(source)
    print("Day 19")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

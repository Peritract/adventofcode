from operator import mul, add
import re

def load_input(source="input.txt", dim=3):
    with open(source, 'r') as file:
        return [x.strip() for x in file]

ops = {"+": add, '*': mul}
    
def basic_solve(num_str):
    tokens = num_str.split(" ")
    answer = int(tokens[0])
    op = None
    for token in tokens[1:]:
        if token.isnumeric():
            val = int(token)
            answer = ops[op](answer, val)
        else:
            op = token
    return answer

def solve(num_str, comp=False):
    new_str = num_str
    while new_str.count("(") > 0:
        matches = re.findall(r"(\([\d+*\s]+\))", new_str)
        for match in matches:
            if comp:
                ans = str(complex_solve(match[1:-1]))
            else:    
                ans = str(basic_solve(match[1:-1]))
            new_str = new_str.replace(match, ans)
    if comp:
        return complex_solve(new_str)
    return basic_solve(new_str)

def first_star(data):
    result = 0
    for line in data:
        result += solve(line)
    return result

def complex_solve(num_str):
    new_str = num_str
    while new_str.count("+") > 0:
        matches = re.findall(r"(\d+( \+ \d+)+)", new_str)
        for match in matches:
            ans = str(basic_solve(match[0]))
            if new_str.count(match[0]) > 1:
                new_str = new_str.replace(match[0] + " ", ans + " ")
            else:
                new_str = new_str.replace(match[0], ans)
    ans = basic_solve(new_str)
    return ans

def second_star(data):
    result = 0
    for line in data:
        val = solve(line, comp=True)
        with open('results.txt', 'a') as file:
            file.write(str(val) + "\n")
        result += val
    return result
    
def solution(source):
    data = load_input(source)
    print("Day 18")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

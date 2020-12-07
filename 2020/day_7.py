import re

def parse_bag_line(line):
    if "no other" in line:
        return None
    bags = re.split("bags?[\.,]?", line)
    contents = []
    for x in bags:
        if len(x) > 1:
            bag = x.strip().split()
            bag = (" ".join(bag[1:]), int(bag[0]))
            contents.append(bag)
    return contents
            
def load_input(source="input.txt"):
    with open(source, 'r') as file:
        bags = {}
        for line in file.readlines():
            key = line.split(" bags ")[0]
            contents = parse_bag_line(line.split(" contain ")[1].strip())
            bags[key] = contents
    
    return bags

def unravel(key, data):
    if data[key] == None:
        return 0
    elif key == "shiny gold":
        return 0
    count = 0
    if "shiny gold" in [x[0] for x in data[key]]:
        return 1
    for x in data[key]:
        if x != ["shiny gold"]:
            count += unravel(x[0], data)
    if count > 0:
        return 1
    
    return 0

def ravel(key, data):
    if data[key] == None:
        return 1
    else:
        count = 1
        for x in data[key]:
            count += x[1] * ravel(x[0], data)
        return count
        
def first_star(data):
    count = 0
    
    for x in data:
        count += unravel(x, data)
    
    return count
        

def second_star(data):
    return ravel("shiny gold", data) - 1
    
def solution(source):
    data = load_input(source)
    print("Day 7")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

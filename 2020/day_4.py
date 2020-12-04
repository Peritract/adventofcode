import re

def load_input(source="input.txt"):
    with open(source, 'r') as file:
        details = file.read().split("\n\n")
    return [{y.split(":")[0] : y.split(":")[1]
             for y in x.replace("\n", " ").split(" ")} for x in details]
        
def is_valid(passport):
    keys = sorted(passport.keys())
    if keys == ['byr', 'cid', 'ecl', 'eyr',
                'hcl', 'hgt', 'iyr', 'pid'] or keys == ['byr', 'ecl', 'eyr',
                                                        'hcl', 'hgt', 'iyr',
                                                        'pid']:
        return True
    
    return False
               
def is_correct(pp):
    if len(pp["byr"]) != 4 or not 1920 <= int(pp["byr"]) <= 2002:
        return False
    if len(pp["iyr"]) != 4 or not 2010 <= int(pp["iyr"]) <= 2020:
        return False
    if len(pp["eyr"]) != 4 or not 2020 <= int(pp["eyr"]) <= 2030:
        return False
    if pp["ecl"] not in "amb blu brn gry grn hzl oth":
        return False
    if len(pp["pid"]) != 9 or not pp["pid"].isnumeric():
        return False
    if pp["hgt"][-2:] not in ["cm", "in"]:
        return False
    
    if pp["hgt"][-2:] == "in":
        if not 59 <= int(pp["hgt"][:-2]) <= 76:
            return False
    else:
        if not 150 <= int(pp["hgt"][:-2]) <= 193:
            return False
        
    if pp["hcl"][0] != "#" or len(pp["hcl"][1:]) != 6:
        return False
    
    col_num = pp["hcl"][1:]

    if not re.match("[a-z0-9]{6}", col_num):
        return False
    
    return True
        
def first_star(data):
    valid = 0
    
    for passport in data:
        if is_valid(passport):
            valid += 1
        
    return valid

def second_star(data):
    valid = 0
    for passport in data:
        if is_valid(passport) and is_correct(passport):
            valid += 1
            
    return valid
    
def solution(source):
    data = load_input(source)
    print("Day 4")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

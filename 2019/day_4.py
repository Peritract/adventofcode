def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data

def is_valid(number):
    digits = str(number)
    check = False
    for i in range(0, len(digits) - 1):
        if int(digits[i]) > int(digits[i + 1]):
            return False
        elif digits[i] == digits[i + 1]:
            check = True
    if digits[-1] < digits[-2]:
        return False
    if check == True:
        return True

def find_double(digits):
    for i in range(0, len(digits)-1):
        if digits[i] == digits[i+1]:
            if i+2 >= len(digits) or digits[i] != digits[i+2]:
                if i-1 < 0 or digits[i] != digits[i-1]:
                    return True
    return False

def is_complex_valid(number):
    digits = str(number)
    for i in range(0, len(digits) - 1):
        if int(digits[i]) > int(digits[i + 1]):
            return False
    if digits[-1] < digits[-2]:
        return False
    if find_double(digits):
        return True
    return False

def first_star(data):
    start, stop = map(int, data.split("-"))
    count = 0
    for i in range(start, stop + 1):
        if is_valid(i):
            count += 1
    return count

def second_star(data):
    start, stop = map(int, data.split("-"))
    count = 0
    for i in range(start, stop + 1):
        if is_complex_valid(i):
            count += 1
    return count

def solution(source):
    data = load_input(source)
    print("Day 4")
    print("First star:", first_star(data))
    print("Second star:", second_star(data))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

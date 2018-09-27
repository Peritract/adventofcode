def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line)
    if len(data) == 1:
        data = data[0]
    return data

def wrong_pairs(text):
    if "ab" in text or "cd" in text or "pq" in text or "xy" in text:
        return True
    else:
        return False

def double(text):
    for i in range(0, len(text) - 1):
        if text[i] == text[i+1]:
            return True
    return False

def sufficient_vowels(text):
    vowels = 0
    for i in text:
        if i in "aeiou":
            vowels += 1
    if vowels > 2:
        return True
    else:
        return False

def pair(text):
    for i in range(0, len(text) - 2):
        if text[i] == text[i+2]:
            return True
    return False

def pairs(text):
    for i in range(0, len(text) - 4):
        for j in range(i+2, len(text)-2):
            if text[i:i+2] == text[j:j+2]:
                return True
    return False

def first_star(data):
    num = 0
    for line in data:
        if sufficient_vowels(line) and double(line) and not wrong_pairs(line):
            num += 1
    return num

def second_star(data):
    num = 0
    for line in data:
        if pair(line) and pairs(line):
            num += 1
    return num

def solution(source):
    data = load_input(source)
    print("Day 5")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data
    

def first_star(data):
    two = 0
    three = 0
    two_check = False
    three_check = False
    for i in data:
        letters = {}
        for j in i:
            if j in letters:
                letters[j] += 1
            else:
                letters[j] = 1
        for key, value in letters.items():
            if value == 2:
                two_check = True
            elif value == 3:
                three_check = True
        if two_check:
            two += 1
            two_check = False
        if three_check:
            three += 1
            three_check = False
    return two * three

def find_match(a, b):
    #Returns True for two strings with only one difference
    diffs = 0
    index = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diffs += 1
            index = i
    if diffs != 1:
        return False
    return a[:index] + a[index+1:]

def second_star(data):
    answer = False
    for i in range(len(data)):
        for j in range(i + 1, len(data) - 1):
            answer = find_match(data[i], data[j])
            if answer:
                return answer

def solution(source):
    data = load_input(source)
    print("Day 2")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

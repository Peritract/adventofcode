def load_input(source):
    with open('input.txt', 'r') as file:
        lines = []
        for x in file.readlines():
            words = x.split(" ")
            nums = [int(y) for y in words[0].split("-")]
            char = words[1][0]
            pw = words[2].strip()
            lines.append((nums[0], nums[1], char, pw))
    return lines

def first_star(data):
    count = 0
    for line in data:
        if line[0] <= line[3].count(line[2]) <= line[1]:
            count += 1
    return count
            
def second_star(data):
    count = 0
    for line in data:
        if line[3][line[0] - 1] == line[2] or line[3][line[1] - 1] == line[2]:
            if not line[3][line[0] - 1] == line[3][line[1] - 1]:
                count += 1
    return count

def solution(source):
    data = load_input(source)
    print("Day 2")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

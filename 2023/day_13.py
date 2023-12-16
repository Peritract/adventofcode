def load_input(source):
    with open(source) as f:
        data = [[list(r) for r in x.strip().split("\n")] for x in f.read().split("\n\n")]
    if len(data) == 1:
        data = data[0]
    return data

def display_grid(grid):
    for y in grid:
        print("".join(y))
    print("")
    
def find_reflection(pattern):
    possible = None
    lines = []
    for i in range(len(pattern) -1):
        if pattern[i] == pattern[i + 1]:
            possible = (i, i + 1)
            u, d = i - 1, i + 2
            while u >= 0 and d < len(pattern):
                if pattern[u] == pattern[d]:
                    u -= 1
                    d += 1
                else:
                    possible = None
                    break
            if possible is not None:
                lines.append(possible)
    return lines if len(lines) > 0 else None

def transpose(pattern):
    rows = []
    for x in range(len(pattern[0])):
        row = ""
        for y in range(len(pattern)):
            row += pattern[y][x]
        rows.append(row)
    return rows

def first_star(data):
    tot = 0
    for pattern in data:
        if ver := find_reflection(transpose(pattern)):
            # print(ver, ver[0] + 1)
            tot += ver[0][0] + 1
        elif hor := find_reflection(pattern):
            # print(hor, hor[1] * 100)
            tot += (hor[0][1]) * 100
    return tot


def find_reflection_lines(pattern):
    lines = []
    if ver := find_reflection(transpose(pattern)):
        for l in ver:
            lines.append(("V", l))
    if hor := find_reflection(pattern):
        for l in hor:
            lines.append(("H", l))
    return lines

    
def check_smudges(pattern, original):
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            
            pattern[y][x] = "." if pattern[y][x] == "#" else "#"
            lines = find_reflection_lines(pattern)
            for l in lines:
                if l not in original:
                    return l
            pattern[y][x] = "." if pattern[y][x] == "#" else "#"

def second_star(data):
    tot = 0
    for pattern in data:
        lines = find_reflection_lines(pattern)
        res = check_smudges(pattern, lines)
        if res[0] == "V":
            tot += res[1][0] + 1
        else:
            tot += res[1][1] * 100
    return tot


def solution(source):
    data = load_input(source)
    print("Day 13")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

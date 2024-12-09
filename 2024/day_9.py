def load_input(source):
    with open(source) as f:
        data = [int(x) for x in f.read().strip()]
    return data

def get_disk_map(data):
    file_mode = True
    curr_file = 0
    disk_map = []
    for c in data:
        if file_mode:
            for i in range(c):
                disk_map.append(curr_file)
            curr_file += 1
        else:
            disk_map.extend(list('.' * c))
        file_mode = not file_mode
    return disk_map

def get_checksum(dm):
    return sum(int(dm[i]) * i for i in range(len(dm)) if dm[i] != '.')

def first_star(data):
    dm = get_disk_map(data)
    p1, p2 = 0, len(dm) - 1
    while p1 < p2:
        if dm[p1] == ".":
            dm[p1], dm[p2] = dm[p2], dm[p1]
            p2 -= 1
        else:
            p1 += 1
    return get_checksum(dm)

def get_first_blank_of_length(dm, length, limit):
    for i in range(len(dm)):
        if dm[i] == ".":
            if all([dm[x] == "." and x < limit for x in range(i, min(i + length, limit, len(dm) - 1))]) and len(dm[i: min(i + length, limit, len(dm) - 1)]) == length:
                return i, i + length - 1
    raise ValueError("Unable to identify blank.")

def second_star(data):
    dm = get_disk_map(data)
    t, h = len(dm) -1, len(dm) - 1
    moved = []
    while h >= -1:
        if dm[h] == dm[t]:
            h -= 1
        else:
            start, end = h + 1, t
            f_length = end + 1 - start
            if dm[start] != "." and dm[start] not in moved:
                try:
                    b_start, b_end = get_first_blank_of_length(dm, f_length, start)
                    for i in range(f_length):
                        dm[b_start + i], dm[start + i] = dm[start + i], dm[b_start + i]
                    moved.append(dm[b_start])
                except ValueError:
                    pass
            t = h
    return get_checksum(dm)

def solution(source):
    data = load_input(source)
    print("Day 9")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

NUM_WORDS = {"nine": "9", "eight": "8",  "seven": "7",
             "six": "6", "five" : "5", "four": "4",
             "three": "3", "two": "2", "one" : "1"
             }

OPTIONS = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
            'nine', 'eight', 'seven', 'six', 'five',
                'four', 'three', 'two', 'one']

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    return data


def is_possible_num_word(word):
    poss = False
    for k in NUM_WORDS.keys():
        if k.startswith(word):
            poss = True
    return poss


def replace_num_words(row):
    res = ""
    acc = ""
    for c in row:
        if c.isdigit():
            res += c
            if acc in NUM_WORDS:
                res += NUM_WORDS[acc]
            acc = ""
        else:
            acc += c
            if acc in NUM_WORDS:
                res += NUM_WORDS[acc]
                if is_possible_num_word(acc[-1]):
                    acc = c
                else:
                    acc = ""
            elif not is_possible_num_word(acc):
                
                acc = c
    return res


def get_by_replacement(data):
    # Doesn't work
    tot = 0
    for r in data:
        r1 = replace_num_words(r)
        tot += int(r1[0] + r1[-1])
    return tot


def get_by_index(row):
    min_index = None
    min_val = None
    for opt in OPTIONS:
        idx = row.find(opt)
        if idx != -1 and (min_index is None or idx < min_index):
            min_val = opt
            min_index = idx
    if min_val:
        return min_val if min_val.isdigit() else NUM_WORDS[min_val]


def first_star(data):
    data = [[d for d in row
             if d.isdigit()]
             for row in data]
    return sum(map(lambda r: int(r[0] + r[-1]), data))


def second_star(data):
    tot = 0
    for r in data:
        r0 = get_by_index(r)
        r1 = None
        start_idx = -1
        while not r1:
            r1 = get_by_index(r[start_idx:])
            start_idx -= 1
        tot += int(r0 + r1)
    return tot

def solution(source):
    data = load_input(source)
    print("Day 1")
    #print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

# 54181
# 54156
# 54126
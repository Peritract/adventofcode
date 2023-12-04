def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data

def parse_lines(data, with_nums=False):
    parsed = []
    games = {}
    for l in data:
        _, num_lists = l.split(": ")
        card = [[int(x)
                for x in sl.split()]
                for sl in num_lists.split(" | ")]
        if not with_nums:
            parsed.append(card)
        else:
            games[int(_.split()[1])] = {
                "prizes" : card[0],
                "nums" : card[1],
                "quant" : 1
            }
    return parsed if not with_nums else games

def first_star(data):
    cards = parse_lines(data)
    total = 0

    for c in cards:
        matches = len([x for x in c[1] if x in c[0]])
        total += 2**(matches-1) if matches else 0

    return total


def second_star(data):
    games = parse_lines(data, with_nums=True)
    for i in range(1, max(games.keys())):
        g = games[i]
        wins = len([x for x in g['nums']
                    if x in g['prizes']])
        for q in range(1, wins + 1):
            games[i+q]["quant"] += g['quant']
    return sum([x["quant"] for x in games.values()])


def solution(source):
    data = load_input(source)
    print("Day N")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

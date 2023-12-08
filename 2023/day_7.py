from functools import cmp_to_key

HAND_ORDER = ["5K", "4K", "FH", "3K", "2P", "1P", "HC"]
CARD_ORDER = "AKQJT98765432"
JOKER_CARD_ORDER = "AKQT98765432J"

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data
    

def parse_input(data):
    return [{"h": r.split()[0], "b": int(r.split()[1])} for r in data]


def get_hand_type(cards, joker=False):
    card_counts = sorted([(c, cards.count(c)) for c in set(cards)], key=lambda x: x[1], reverse=True)
    counts = [c[1] for c in card_counts]
    if joker and "J" in cards:
        print(cards)
        most_common = card_counts[0][0] if card_counts[0][0] != "J" or cards == "JJJJJ" else card_counts[1][0]
        cards = cards.replace("J" , most_common)
        counts = [cards.count(c) for c in set(cards)]
    if 5 in counts:
        return "5K"
    elif 4 in counts:
        return "4K"
    elif 3 in counts and 2 in counts:
        return "FH"
    elif 3 in counts:
        return "3K"
    elif counts.count(2) == 2:
        return "2P"
    elif 2 in counts:
        return "1P"
    else:
        return "HC"
    
def compare_rounds(r1, r2, jokers=False):
    h1 = HAND_ORDER.index(r1["t"])
    h2 = HAND_ORDER.index(r2["t"])
    if h1 < h2:
        return -1
    elif h1 > h2:
        return 1
    else:
        for i in range(len(r1["h"])):
            order = CARD_ORDER if not jokers else JOKER_CARD_ORDER
            c1 = order.index(r1["h"][i])
            c2 = order.index(r2["h"][i])
            if c1 < c2:
                return -1
            elif c1 > c2:
                return 1
        return 0


def first_star(data):
    data = parse_input(data)
    for r in data:
        r["t"] = get_hand_type(r["h"])
    rounds = sorted(data, key=cmp_to_key(compare_rounds),
                    reverse=True)
    return sum([r["b"] * (i + 1)
                for i, r in
                enumerate(rounds)])


def second_star(data):
    data = parse_input(data)
    for r in data:
        r["t"] = get_hand_type(r["h"], True)
    rounds = sorted(data, key=cmp_to_key(lambda a, b: compare_rounds(a, b, True)),
                    reverse=True)
    return sum([r["b"] * (i + 1)
                for i, r in
                enumerate(rounds)])


def solution(source):
    data = load_input(source)
    print("Day 7")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

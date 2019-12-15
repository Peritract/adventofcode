import math

def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data


def parse_reactions(data):
    reactions = {}
    for line in data:
        raw = line.split(" => ")
        result = raw.pop(-1).split(" ")
        components = raw[0].split(", ")
        reactions[result[1]] = {"amt": int(result[0]),
                                "reqs": {x.split(" ")[1]: int(x.split(" ")[0]) 
                                         for x in components}}
    return reactions


def create_material(target, reactions, materials, amount=1):
    # Get the requirements
    reqs = reactions[target]["reqs"]
    start = materials[target]
    amt = reactions[target]["amt"]
    if amount > 1:
        reqs = {x: reqs[x] * amount for x in reqs}
        amt = amt * amount
    while materials[target] == start:
        # Try and make it based on the current materials
        if all(materials[x] - reqs[x] >= 0 for x in reqs):
            for x in reqs:
                materials[x] -= reqs[x]
            materials[target] += amt
            return materials

        # If it can't be made at present
        for x in reqs:
            if materials[x] - reqs[x] < 0:
                needed = reqs[x] - materials[x]
                if x == "ORE":
                    materials["COST"] += needed
                    materials["ORE"] += needed
                else:
                    needed = math.ceil((reqs[x] - materials[x]) / reactions[x]["amt"])
                    materials = create_material(x, reactions, materials, needed)

    # Once the number created has increased,
    # return the current set of materials
    return materials


def first_star(data):
    reactions = parse_reactions(data)
    reactions["ORE"] = {"amt": 1, "reqs": {}}
    materials = {x: 0 for x in reactions}
    materials["ORE"] = 0
    materials["COST"] = 0
    return create_material("FUEL", reactions, materials)["COST"]


def second_star(data):
    reactions = parse_reactions(data)
    reactions["ORE"] = {"amt": 1, "reqs": {}}
    materials = {x: 0 for x in reactions}
    materials["ORE"] = 0
    materials["COST"] = 0
    cost = 0
    low = 2
    high = 1000000000000
    mid = int(low + (high - low)/2)
    last = None
    while low < high:
        materials = {x: 0 for x in reactions}
        materials["ORE"] = 0
        materials["COST"] = 0
        last = cost
        cost = create_material("FUEL", reactions, materials, mid)["COST"]
        if cost == last:
            return mid
        elif cost < 1000000000000:
            low = mid
            mid = int(low + (high - low)/2)
        else:
            high = mid
            mid = int(low + (high - low)/2)
    return mid






def solution(source):
    data = load_input(source)
    print("Day 14")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

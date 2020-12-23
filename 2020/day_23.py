# Had to learn a new way of thinking about things for part 2; basically linked lists but you store them in a dict so traversal is not required.

def load_input(source="input.txt"):
    with open(source, 'r') as file:
        return [int(x) for x in file.read().strip()]
    
def pick_up(data, index):
    pickup = []
    
    while len(pickup) < 3:
        if index >= len(data):
            index = 0
        pickup.append(data.pop(index))
    
    return pickup

def find_destination(data, curr):
    drop = curr - 1
    found = False
    while not found:
        try:
            dest = data.index(drop)
            found = True
        except:
            drop -= 1
            if drop < min(data):
                drop = max(data)
    return dest

def get_order(data):
    index = data.index(1)
    order = data[index:] + data[:index]
    return "".join([str(x) for x in order[1:]])

def cups(data, rounds=10):
    turn = 0
    curr = data[0]
    
    while turn < rounds:
        pickup = pick_up(data, data.index(curr) + 1)
        drop = find_destination(data, curr)
        data = data[:drop + 1] + pickup + data[drop + 1:]
        curr = data[data.index(curr) + 1 if data.index(curr) < len(data) - 1 else 0]
        turn += 1
    return data
        
def first_star(data):
    return get_order(cups(data, 100))

def cups2(cups, start, rounds=10):
    turn = 0
    curr = start
    
    while turn < rounds:
        # Get the next three values
        one = cups[curr]
        two = cups[one]
        three = cups[two]
        
        # Paper over the cut
        cups[curr] = cups[three]
        
        # Find where to place the three
        drop = curr - 1
        while drop in [one, two, three] or drop < 1:
            drop -= 1
            if drop < 1:
                drop = max(cups.values())
        # Make the update
        temp = cups[drop]
        cups[drop] = one
        cups[three] = temp
        
        # Update the current position
        curr = cups[curr]
        
        # Increment the turn
        turn += 1
    return cups

def get_order2(cups, start=1):
    val = cups[start]
    nums = [str(val)]
    while val != start:
        nums.append(str(cups[val]))
        val = cups[val]
    return "".join(nums[:-1])
        
def second_star(data):
    cups = {}
    for i in range(len(data) - 1):
        cups[data[i]] = data[i + 1]
    cups[data[-1]] = 10
    for i in range(10, 1000000):
        cups[i] = i + 1
    cups[1000000] = data[0]
    results = cups2(cups, data[0], 10000000)
    
    one = results[1]
    two = results[one]
    
    return one * two
    
def solution(source):
    data = load_input(source)
    print("Day 23")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

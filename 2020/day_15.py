def load_input(source="input.txt"):
    with open(source, 'r') as file:
        return [int(x) for x in file.read().strip().split(",")]

def first_star(data, limit=2020):
    turn = len(data) + 1
    mem = {x: i + 1 for i, x in enumerate(data)}
    seen = {x for x in data[:-1]}
    prev = data[-1]

    while turn <= limit:
        # If the number has not been considered before
        if prev not in seen:
            seen.add(prev)
            
            mem[prev] = turn - 1
            
            # Unseen before, so zero
            prev = 0
        
        # If we need to look at it again
        else:
            new = turn - 1 -  mem[prev]
            mem[prev] = turn - 1
            prev = new
            
        turn += 1

    return prev
    
def second_star(data):
    return first_star(data, 30000000)
    
def solution(source):
    data = load_input(source)
    print("Day 15")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

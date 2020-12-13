# I did need quite a bit of help with this one, to see the patterns in the maths. The code is mine though.

from functools import reduce

def load_input(source="input.txt"):
    with open(source, 'r') as file:
        time = file.readline()
        buses = file.readline()
        return [int(time.strip()), [int(val) if val != 'x' else 'x' for val in buses.strip().split(',')]]
    
def first_star(data):
    data[1] = sorted(filter(lambda x: x != 'x', data[1]), reverse=True)
    nexts = []
    for x in data[1]:
        next_start = 0
        times = 0
        while next_start < data[0]:
            next_start += x
            times += 1
        nexts.append(next_start)
    return (min(nexts) - data[0]) * data[1][nexts.index(min(nexts))]

def prep_data(data):
    result = []
    for i, x in enumerate(data):
        if x != 'x':
            result.append((x, i))
    return result

def calculate(arr):
    index = 2
    start = arr[0][0]
    inc = arr[0][0]
    # As long as there are still values to consider
    while index <= len(arr):
        # Grab a set of values
        vals = arr[:index]
        # Start looking for a match
        match = False
        while not match:
            
            # Check the next valid number
            start += inc
            
            check_vals = [start + x[1] for x in vals]
            if all([check_vals[i] % vals[i][0] == 0 for i in range(len(vals))]):
                inc = reduce(lambda a, b: a * b, [x[0] for x in vals])
                match = True
                index += 1
    return(start)

def second_star(data):
    return calculate(prep_data(data[1]))
    
def solution(source):
    data = load_input(source)
    print("Day 13")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

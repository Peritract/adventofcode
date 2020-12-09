from itertools import combinations

def load_input(source="input.txt"):
    with open(source, 'r') as file:
        return [int(x.strip()) for x in file.readlines()]
        
def find_sum(x, arr):
    for i in arr[:-1]:
        for j in arr[1:]:
            if i + j == x and i != j:
                return True
    return False
    
def first_star(data, offset=25):
    for i in range(offset, len(data)):
        if not find_sum(data[i], data[i - offset:i]):
            return data[i]
    return -1
        

def second_star(data):
    target = first_star(data)
    combinations = []
    
    # Check all combination lengths
    for i in range(len(data) - 1, 2, -1):
        
        # For each length, build contiguous lists
        for j in range(0, len(data) - i):
            arr = data[j: j + i]
            if sum(arr) == target:
                return min(arr) + max(arr)

            
def solution(source):
    data = load_input(source)
    print("Day 9")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

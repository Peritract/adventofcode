import re

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data
    
def preprocess_data(data):
    return [[int(x) for x in l] for l in data]

def get_largest_number_2d(bank: list[int]) -> int:
    """Return the largest 2-digit number without rearrangment."""
    largest = 0
    second = 0
    largest_i = 0
    for i, p in enumerate(bank):
        if p > largest and i != len(bank) - 1:
            largest = p
            largest_i = i
    for p in bank[largest_i + 1:]:
        if p > second:
            second = p
    
    return int(f"{largest}{second}")

def get_largest_number_12d(bank: list[int]) -> int:

    digits = []
    prev = -1

    while(len(digits)) < 12:
        reserved = 12 - len(digits) - 1
        largest = 0
        for i in range(prev + 1, len(bank) - reserved):
            if bank[i] > largest:
                largest = bank[i]
                prev = i
        digits.append(largest)
    return int("".join(str(x) for x in digits))

def first_star(data):
    joltage = 0
    for b in data:
        val = get_largest_number_2d(b)
        joltage += val
        
    return joltage

def second_star(data):
    joltage = 0
    for b in data:
        val = get_largest_number_12d(b)
        joltage += val
    return joltage

def solution(source):
    data = preprocess_data(load_input(source))
    print("Day 3")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

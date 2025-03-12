from datetime import datetime, timezone
from collections import Counter

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data
    

def is_valid(password: str) -> bool:
    if (
        (4 <= len(password) < 13) and password.lower() != password and password.upper() != password
        and any(x in password for x in "0123456789") and any(ord(x) > 127 for x in password)
        ):
        return True
    return False 


def answer(data):

    return sum(is_valid(d) for d in data)

def solution(source):
    data = load_input(source)
    print("Day 3")
    print("Answer:", str(answer(data)))


if __name__ == "__main__":
    solution("input.txt")

from datetime import datetime, timezone
from collections import Counter

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data
    
def answer(data):

    ans = Counter([datetime.fromisoformat(row).astimezone(timezone.utc)
                   for row in data]).most_common()[0][0]
    return ans.isoformat()

def solution(source):
    data = load_input(source)
    print("Day 2")
    print("Answer:", str(answer(data)))


if __name__ == "__main__":
    solution("input.txt")

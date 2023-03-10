import hashlib

def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line)
    if len(data) == 1:
        data = data[0]
    return data

def first_star(data):
    hashed = "11111"
    num = 0
    while str(hashed[0:5]) != "00000":
        num += 1
        hashed = hashlib.md5(("yzbqklnj" + str(num)).encode("utf-8")).hexdigest()
    return num
        
def second_star(data):
    hashed = "111111"
    num = 0
    while str(hashed[0:6]) != "000000":
        num += 1
        hashed = hashlib.md5(("yzbqklnj" + str(num)).encode("utf-8")).hexdigest()
    return num

def solution(source):
    data = load_input(source)
    print("Day 4")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

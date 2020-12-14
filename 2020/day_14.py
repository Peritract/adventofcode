def load_input(source="input.txt"):
    with open(source, 'r') as file:
        data = [[y for y in x.strip().split(" = ")] for x in file.readlines()]
    for x in range(len(data)):
        if data[x][0][:3] == "mem":
            data[x][0] = int(data[x][0][4:-1])
            data[x][1] = int(data[x][1])
        else:
            data[x] = data[x][1]
    return data

def binify(num):
    return bin(num)[2:].zfill(36)

def intify(bin_str):
    return int(bin_str, 2)

def apply_mask(bin_str, mask):
    result = []
    for x in range(len(mask)):
        if mask[x] != "X":
            result.append(mask[x])
        else:
            result.append(bin_str[x])
    return "".join(result)

def first_star(data):
    mem = {}
    mask = None
    for cmd in data:
        if type(cmd) == str:
            mask = cmd
        else:
            mem[cmd[0]] = intify(apply_mask(binify(cmd[1]), mask))
    return sum(mem.values())

def get_combinations(num):
    nums = []
    for i in range(0, 2**num):
        b = bin(i)[2:]
        nums.append(str(b).zfill(num))
    return nums
        
def get_mem_variations(mask, address):
    result = []
    # put the nums in
    for x in range(len(mask)):
        if mask[x] != "X":
            if mask[x] == "1":
                result.append("1")
            else:
                result.append(address[x])
        else:
            result.append(address[x])
    
    result = "".join(result)
    print(address)
    print(mask)
    print(result)
    # Get the possible x options
    x = get_combinations(mask.count("X"))
    results = []
    
    # for possible variation set
    for vari in x:
        index = 0
        temp = []
        for l in mask:
            if l == "X":
                temp.append(vari[index])
                index += 1
            else:
                temp.append(l)
        temp = "".join(temp)
        results.append(temp)
    
    return results

def second_star(data):
    mem = {}
    mask = None
    for cmd in data:
        if type(cmd) == str:
            mask = cmd
        else:
            addresses = get_mem_variations(mask, binify(cmd[0]))
            for x in addresses:
                mem[intify(x)] = cmd[1]
    print(mem)
    
def solution(source):
    data = load_input(source)
    print("Day 14")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

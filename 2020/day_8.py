def load_input(source="input.txt"):
    with open(source, 'r') as file:
        code = list(map(lambda x: [x.split()[0], int(x.split()[1])], file.readlines()))
    return code
        
def first_star(data):
    cnt = 0
    acc = 0
    seen = []
    while cnt < len(data):
        if cnt not in seen:
            seen.append(cnt)
            if data[cnt][0] == "nop":
                cnt += 1
            elif data[cnt][0] == "acc":
                acc += data[cnt][1]
                cnt += 1
            else:
                cnt += data[cnt][1]
        else:
            return acc
    else:
        return "Halted", acc
        

def second_star(data):
    for i in range(len(data)):
        if data[i][0] in ["jmp", "nop"]:
            test = load_input()
            test[i][0] = "jmp" if test[i][0] == "nop" else "nop"
            result = first_star(test)
            if type(result) != int:
                return result[1]
            
    
def solution(source):
    data = load_input(source)
    print("Day 8")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

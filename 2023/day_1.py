NUM_WORDS = {"nine": "9", "eight": "8",  "seven": "7",
             "six": "6", "five" : "5", "four": "4",
             "three": "3", "two": "2", "one" : "1"
             }


def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    return data


def extract_calibration_val(row):
    nums = []
    for i in range(len(row)):
        if row[i].isdigit():
            nums.append(row[i])
        else:
            for j in range(i + 2, i + 6):
                if row[i:j] in NUM_WORDS:
                    nums.append(NUM_WORDS[row[i:j]])
                    break
    return int(nums[0] + nums[-1])


def first_star(data):
    data = [[d for d in row
             if d.isdigit()]
             for row in data]
    return sum(map(lambda r: int(r[0] + r[-1]), data))


def second_star(data):
    return sum([extract_calibration_val(r)
                for r in data])
    

def solution(source):
    data = load_input(source)
    print("Day 1")
    #print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

# 54181
# 54156
# 54126
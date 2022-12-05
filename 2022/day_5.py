from copy import deepcopy

def load_input(filename):
  with open(filename) as f_obj:
    return process_input(f_obj.read())

def process_input(data):
    setup, instructions = [x.split("\n") for x in data.split("\n\n")]
    columns = {}
    for i in range(1, len(setup[0]), 4):
        columns[int(setup[-1][i])] = [x[i] for x in setup[:-1] if x[i] != " "]
    instructions = [y.split(" ") for y in instructions]
    instructions = [{"src": int(y[3]),
                     "dst": int(y[5]),
                     "qnt": int(y[1]),
                     } for y in instructions]
    return {
        "columns": columns,
        "instructions": instructions
    }

def first_star(data):
    for i in data["instructions"]:
        for r in range(i["qnt"]):
            mv = data["columns"][i["src"]].pop(0)
            data["columns"][i["dst"]].insert(0, mv)
    ans = "".join([v[0] for k,v in data["columns"].items()])
    return ans

def second_star(data):
    for i in data["instructions"]:
        mv = []
        for r in range(i["qnt"]):
            mv.append(data["columns"][i["src"]].pop(0))
        data["columns"][i["dst"]] = mv + data["columns"][i["dst"]]
    ans = "".join([v[0] for k,v in data["columns"].items()])
    return ans

if __name__ == "__main__":
  data = load_input("input.txt")
  print("First star:", first_star(deepcopy(data)))
  print("Second star:", second_star(data))

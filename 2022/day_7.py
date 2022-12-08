def load_input(filename):
  with open(filename) as f_obj:
    return parse_nodes([x.strip() for x in f_obj.readlines()])

class Node:

    def __init__(self, route, children=[], parent=None):
        self.route = route
        self.children = children
        self.parent = parent

    def __repr__(self):
        return self.route

    def get_size(self):
        return sum([x if type(x) != Node else x.get_size() for x in self.children])


def parse_nodes(data):
    head = Node(route="/")
    nodes = [head]
    curr = head
    i = 0
    while i < len(data):
        if data[i][0] == "$":
            if data[i] == "$ cd /":
                curr = head
            elif data[i] == "$ cd ..":
                curr = curr.parent
            elif data[i] != "$ ls":
                curr = [x for x in curr.children if type(x) == Node and x.route == data[i].split(" ")[2]][0]
        else:
            n = data[i]
            if n[0] == "d":
                n = Node(route=n.split(" ")[1], children=[], parent=curr)
                nodes.append(n)
            else:
               n = int(n.split(" ")[0])
            curr.children.append(n)
        i += 1
    return nodes

def first_star(data):
    return sum([x.get_size() for x in data if x.get_size() <= 100000])

def second_star(data):
    tot = 70000000
    need = 30000000 - (tot - data[0].get_size())
    return min([x.get_size() for x in data if x.get_size() >= need])

if __name__ == "__main__":
  data = load_input("input.txt")
  print("First star:", first_star(data))
  print("Second star:", second_star(data))

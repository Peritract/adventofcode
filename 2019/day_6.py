def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data

class Node:
    def __init__(self, name=None, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
    
    def __str__(self):
        if self.parent:
            return f"{self.name}, orbiting {self.parent}"
        else:
            return self.name

    def count_steps(self, count):
        return count + sum([x.count_steps(count + 1) for x in self.children])

    def find_node(self, name):
        if name == self.name:
            return self
        else:
            routes = [x.find_node(name) for x in self.children]
            for x in routes:
                if x != None:
                    return x
        return None

    def is_descendant(self, target):
        if self.name == target:
            return True
        else:
            routes = [x.is_descendant(target) for x in self.children]
            for x in routes:
                if x:
                    return True
        return False

    def find_lowest_common_ancestor(self, a, b):
        if self.name == a or self.name == b:
            return self
        else:
            for child in self.children:
                if child.is_descendant(a) and child.is_descendant(b):
                    return child.find_lowest_common_ancestor(a, b)
        return self

    def count_path_to_child(self, target):
        if self.name == target:
            # Don't count the ship itself as an orbital jump
            return -1
        else:
            for child in self.children:
                if child.is_descendant(target):
                    return 1 + child.count_path_to_child(target)


def construct_orbital_tree(data):
    links = [x.split(")") for x in data]
    nodes = {}
    for core, satellite in links:
        coreNode = nodes[core] if core in nodes else Node(core)
        satelliteNode = nodes[satellite] if satellite in nodes else Node(satellite, coreNode)
        coreNode.children.append(satelliteNode)
        satelliteNode.parent = coreNode
        if satellite not in nodes:
            nodes[satellite] = satelliteNode
        if coreNode.name not in nodes:
            nodes[core] = coreNode
    return nodes["COM"]

def first_star(data):
    root = construct_orbital_tree(data)
    return root.count_steps(0)

def second_star(data):
    root = construct_orbital_tree(data)
    LCA = root.find_lowest_common_ancestor("YOU","SAN")
    return LCA.count_path_to_child("YOU") + LCA.count_path_to_child("SAN")

def solution(source):
    data = load_input(source)
    print("Day 6")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

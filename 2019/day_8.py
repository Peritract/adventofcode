import itertools

def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data

def split_layers(data, x, y):
    layers = []
    size = x * y
    start = 0
    stop = size
    while stop <= len(data):
        layers.append(data[start:stop])
        start = stop
        stop = stop + size
    return layers

def create_layer(digits, width, height):
    digit = 0
    layer = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(digits[digit])
            digit += 1
        layer.append(row)
    return layer

def get_pixel_from_layers(layers, x, y):
    for z in layers:
        if z[y][x] != "2":
            return z[y][x]

def generate_image_from_layers(layers, width, height):
    final = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(get_pixel_from_layers(layers, x, y))
        final.append(row)
    return final

def first_star(data):
    layers = split_layers(data, 25, 6)
    zero_count = [x.count("0") for x in layers]
    layer = zero_count.index(min(zero_count))
    return layers[layer].count("1") * layers[layer].count("2")

def second_star(data):
    layers = split_layers(data, 25, 6)
    layers = [create_layer(x, 25, 6) for x in layers]
    final = generate_image_from_layers(layers, 25, 6)
    final = "\n" + "".join(["".join(x) + "\n" for x in final])
    return final

def solution(source):
    data = load_input(source)
    print("Day 8")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

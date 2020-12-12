def load_input(source="input.txt"):
    with open(source, 'r') as file:
        return [(line[0], int(line[1:])) for line in file.readlines()]

headings = {90: 'E', 0: 'N', 180: 'S', 270: 'W'}

def get_heading(deg):
    return headings[deg % 360]

def move(cmd, ship):
    if cmd[0] == 'N':
        ship[1] -= cmd[1]
    elif cmd[0] == 'S':
        ship[1] += cmd[1]
    elif cmd[0] == 'W':
        ship[0] -= cmd[1]
    elif cmd[0] == 'E':
        ship[0] += cmd[1]
    return ship
    
def first_star(data):
    ship = [0, 0, 90]
    for cmd in data:
        if cmd[0] == 'L':
            ship[2] -= cmd[1]
        elif cmd[0] == 'R':
            ship[2] += cmd[1]
        elif cmd[0] == 'F':
            h = get_heading(ship[2])
            ship = move((h, cmd[1]), ship)
        else:
            ship = move(cmd, ship)
    return abs(ship[0]) + abs(ship[1])

def double_move(ship, waypoint, num):
    for i in range(num):
        ship[0] += waypoint[0]
        ship[1] += waypoint[1]
    return ship

def rotate(w, t):
    turn = 0
    while turn < t[1]:
        if t[0] != 'R':
            w = [w[1], -w[0]]
        else:
            w = [-w[1], w[0]]
        turn += 90
    return w

def second_star(data):
    ship = [0, 0]
    waypoint = [10, -1]
    
    for cmd in data:
        if cmd[0] == 'F':
            ship = double_move(ship, waypoint, cmd[1])
        elif cmd[0] in ['L', 'R']:
            waypoint = rotate(waypoint, cmd)
        else:
            waypoint = move(cmd, waypoint)
        
    return abs(ship[0]) + abs(ship[1])
    
def solution(source):
    data = load_input(source)
    print("Day 12")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

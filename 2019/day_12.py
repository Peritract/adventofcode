from itertools import combinations
from math import gcd

def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data

class Moon:
    def __init__(self, position=(0,0,0), velocity=(0,0,0)):
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.vx = velocity[0]
        self.vy = velocity[1]
        self.vz = velocity[2]

    def __repr__(self):
        return f"pos=<X: {self.x}, Y: {self.y}, Z: {self.z}>, vel=<X: {self.vx}, Y: {self.vy}, Z: {self.vz}>"

    def update_position_by_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def get_potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def get_kinetic_energy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def get_total_energy(self):
        return self.get_kinetic_energy() * self.get_potential_energy()

    def apply_gravity(self, other):
        if self == other:
            return
        if self.x != other.x:
            if self.x > other.x:
                self.vx -= 1
            else:
                self.vx += 1
        if self.y != other.y:
            if self.y > other.y:
                self.vy -= 1
            else:
                self.vy += 1
        if self.z != other.z:
            if self.z > other.z:
                self.vz -= 1
            else:
                self.vz += 1

    def get_pos(self):
        return (self.x, self.y, self.z)

    def get_vel(self):
        return (self.vx, self.vy, self.vz)

def create_moons(coordinates):
    moons = []
    for line in coordinates:
        data = [int(x.split("=")[1]) for x in line[1:-1].split(",")]
        moons.append(Moon(data))
    return moons

def apply_gravity(moons):
    for x, y in combinations(moons, 2):
        x.apply_gravity(y)
        y.apply_gravity(x)

def first_star(data):
    moons = create_moons(data)
    for i in range(1000):     
        apply_gravity(moons)
        for moon in moons:
            moon.update_position_by_velocity()
    return sum([x.get_total_energy() for x in moons])

def find_lcm(arr):

    # Assume it's the first number
    lcm = arr[0]

    # Once for every number in the array
    for i in arr[1:]:

        # Calculate the lcm
        # lcm = num*other_num/GCD(num,other_num)
        lcm = int(lcm * i / gcd(lcm, i))

    return lcm

def solve_axis(data, index):
    moons = create_moons(data)
    step = 0
    while True:
        step += 1
        apply_gravity(moons)
        for i in range(len(moons)):
            moons[i].update_position_by_velocity()
        if all([x.get_vel()[index] == 0 for x in moons]):
            return step

def second_star(data):
    x = solve_axis(data, 0)
    y = solve_axis(data, 1)
    z = solve_axis(data, 2)
    lcm = find_lcm((x,y,z))
    return lcm * 2

def solution(source):
    data = load_input(source)
    print("Day 12")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

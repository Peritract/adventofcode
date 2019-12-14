from int_code_computer import IntCodeComputer
import os
from time import sleep


def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data


def display_screen(screen, score):
    os.system("clear")
    graphics = {0: " ", 1: "\u2588",
                2: "\u001b[34m#\u001b[0m", 3: "\u001b[34m\u2594\u001b[0m",
                4: "\u001b[31m*\u001b[0m"}
    for y in screen:
        print("".join([graphics[x] for x in y]))
    print(f"SCORE: {score}")


def update_game_state(screen, output, score=0):
    for i in range(0, len(output), 3):
        x = output[i]
        y = output[i + 1]
        v = output[i + 2]
        if x == -1 and y == 0:
            score = v
        else:
            screen[y][x] = v

    return score


def get_user_input():
    controls = {"a": -1, "s": 0, "d": 1}
    return controls[input()]


def get_char_x(screen, char):
    for y in screen:
        if char in y:
            return y.index(char)


def calculate_move(current_ball, paddle):
    if current_ball == paddle:
        return 0
    elif current_ball > paddle:
        return 1
    else:
        return -1


def first_star(data):
    arcade = IntCodeComputer(data)
    while not arcade.halt:
        arcade.run()
    count = 0
    screen = [[0 for x in range(44)] for y in range(20)]
    update_game_state(screen, arcade.output_log)
    for y in screen:
        count += y.count(2)
    return count


def second_star(data):
    data = data.copy()
    data[0] = 2
    arcade = IntCodeComputer(data.copy())
    score = 0
    screen = [[0 for x in range(44)] for y in range(20)]
    ball_pos = None
    while not arcade.halt:
        arcade.run()
        score = update_game_state(screen, arcade.output_log, score)
        display_screen(screen, score)
        arcade.output_log = []
        ball_pos = get_char_x(screen, 4)
        paddle = get_char_x(screen, 3)
        move = calculate_move(ball_pos, paddle)
        arcade.add_input(move)
        sleep(0.02)
    return score


def solution(source):
    data = load_input(source)
    data = [int(x) for x in data.split(",")]
    print("Day 13")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

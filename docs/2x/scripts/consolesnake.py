# -*- coding: UTF-8 -*-

__doc__ = """

Draw a controllable snake on the console

@Version: 0.1

@Author: LinYuChen

"""

import platform
import time
import os
from threading import Thread


class Screen(object):

    WIDTH = 30
    HEIGHT = 20
    screen = []
    hit = "input (w | s | a | d) then enter:"

    def __init__(self):
        self.init_screen()

    def init_screen(self):
        self.screen = [["○" for i in range(self.WIDTH)] for i in range(self.HEIGHT)]

    def full_point(self, x, y):
        self.screen[y][x] = "●"

    def full_points(self, pos):
        for i in pos:
            self.full_point(i[0], i[1])

    def draw(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        screen_str = "\n".join(["".join(i) for i in self.screen])
        print(screen_str)
        print(self.hit)


class Snake(Thread, Screen):
    snake_body_pos = [[3, 3], [4, 3], [5, 3], [6, 3]]
    current_direction = "right"
    interval = 0.5

    def __init__(self):
        Screen.__init__(self)
        Thread.__init__(self)

    def __draw_snake(self):
        self.full_points(self.snake_body_pos)

    def __move(self, direction):
        self.current_direction = direction
        new_pos = self.__get_head_pos()
        if direction == "up":
            new_pos[1] -= 1
        elif direction == "down":
            new_pos[1] += 1
        elif direction == "left":
            new_pos[0] -= 1
        elif direction == "right":
            new_pos[0] += 1
        if new_pos[0] >= self.WIDTH or new_pos[0] < 0 or new_pos[1] >= self.HEIGHT or new_pos[1] < 0:
            return

        self.init_screen()
        self.snake_body_pos.pop(0)
        self.snake_body_pos.append(new_pos)
        self.__draw_snake()

    def __get_head_pos(self):
        return self.snake_body_pos[-1][:]

    def move_up(self):
        self.__move("up")

    def move_down(self):
        self.__move("down")

    def move_left(self):
        self.__move("left")

    def move_right(self):
        self.__move("right")

    def __keep_moving(self):
        self.__move(self.current_direction)

    def run(self):
        while True:
            self.__keep_moving()
            self.draw()
            time.sleep(self.interval)


snake = Snake()
snake.start()

while True:
    direction = input()
    if direction == "w":
        snake.move_up()
    elif direction == "s":
        snake.move_down()
    elif direction == "a":
        snake.move_left()
    elif direction == "d":
        snake.move_right()


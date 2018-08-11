# coding=utf-8
import turtle

from datetime import *
import time


def doWork(t):
    turtle.bgcolor("black")  # 修改背景颜色
    sides = 6
    colors = ["red", "yellow", "blue", "green"]
    for x in range(100):
        t.pencolor(colors[x % 4])
        t.forward(x * 3 / sides + x)
        t.left(360 / sides + 1)
        t.width(x * sides / 200)


if __name__ == "__main__":
    t = turtle.Pen()
    doWork(t)

turtle.done()
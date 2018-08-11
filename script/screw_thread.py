# coding=utf-8
import turtle

from datetime import *
import time


def doWork(t):
    colors = ["red", "yellow", "blue", "green"]
    for x in range(100):
        t.pencolor(colors[x % 4])
        t.forward(x)
        t.left(91)


if __name__ == "__main__":
    t = turtle.Pen()
    doWork(t)
    turtle.done()
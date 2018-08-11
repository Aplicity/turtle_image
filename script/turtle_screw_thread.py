# coding=utf-8
import turtle

from datetime import *
import time


def doWork():
    turtle.pensize(2)
    turtle.bgcolor("black")
    turtle.speed(20)
    colors = ["red", "yellow", "purple", "blue"]
    # turtle.tracer(False)
    for x in range(300):
        turtle.forward(2 * x)
        turtle.color(colors[x % 4])
        turtle.left(91)
        # turtle.tracer(True)
        # input()   可以有效解决闪退问题，或者下面的方法


if __name__ == "__main__":
    doWork()
    turtle.done();
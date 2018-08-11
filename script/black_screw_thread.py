# coding=utf-8
import turtle

from datetime import *
import time

def doWork(t):
    turtle.speed(10)

    for x in range(100):
        t.forward(x)
        t.left(91)


if __name__ == "__main__":
    t = turtle.Pen()
    doWork(t)


turtle.done()
# coding=utf-8
import turtle

from datetime import *
import time


def doWork(t):
    for x in range(100):
        t.forward(x)
        t.left(90)


if __name__ == "__main__":
    t = turtle.Pen()
    doWork(t)
    turtle.done()
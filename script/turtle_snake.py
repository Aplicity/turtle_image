# coding=utf-8
import turtle

from datetime import *
import time

#！debug：neckrad report sth wrong。这里注意“：和（）”都是英文格式的才好，中文格式报错。
def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.forward(10)
    turtle.circle(neckrad+1,180)
    turtle.forward(rad*2/3)

def main():
    #turtle.setup(width,height,startx,starty)
    turtle.setup(1300,800,0,0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    #turtle.seth(angle),StandardMode:0 is to east in the right hand,90 is to north in upword.LogoMode:0 to north,90 to east.
    turtle.seth(-40)
    drawSnake(40,80,5,pythonsize/2)

if __name__ == "__main__":
    main()
    turtle.done()
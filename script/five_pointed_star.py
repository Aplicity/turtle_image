# coding=utf-8
import turtle
import time

turtle.pensize(5)          # 线宽
turtle.pencolor("yellow")  # 线的眼神
turtle.fillcolor("red")    # 填充颜色

def draw_5AnglesShape():
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(200)
        turtle.right(144)
    turtle.end_fill()
    time.sleep(2)

def draw_word():           # 写文字
    turtle.penup()
    turtle.goto(-150, -120)
    turtle.color("violet")
    turtle.write("五角星绘制完毕", font=('Arial', 40, 'normal'))

if __name__ == "__main__":
    draw_5AnglesShape()
    draw_word()
    turtle.mainloop()
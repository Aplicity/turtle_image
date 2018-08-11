# coding=utf-8
import turtle
import time

# 同时设置pencolor="red", fillcolor="yellow"
turtle.color("red", "yellow")

# 开始填充
turtle.begin_fill()
for _ in range(50):  # 循环50次, 从0到49
    turtle.forward(200)  # 前行200
    turtle.left(170)  # 左转170°
# 结束填充
turtle.end_fill()

# 不会退出, 而是等待
turtle.mainloop()
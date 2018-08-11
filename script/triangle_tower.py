# encoding: utf8

import turtle

stepSize = 30


def draw1GreenTriangle():
    """ 画有一个绿色的小小三角形
    从图片上看， 整个图形就是由27个小三角形组成的
    """
    global stepSize
    turtle.color("black", "green")  # 笔的颜色的黑色， 填充是绿色
    turtle.begin_fill()  # 开始填充
    turtle.setheading(240)  # 头向左下
    turtle.forward(stepSize)  # 移动指定个单位
    turtle.left(120)  # 逆时针旋转120度
    turtle.forward(stepSize)  # 移动10个单位
    turtle.left(120)  # 逆时针旋转120度
    turtle.forward(stepSize)  # 移动10个单位
    turtle.end_fill()  # 结束填充


def draw3GreenTriangle():
    """ 就是画三个小三角形
    原图片可以看做是9个这样的3个三角形组成的
    """
    draw1GreenTriangle();
    turtle.left(120)  # 逆时针旋转120度
    turtle.forward(stepSize)  # 移动指定单位
    draw1GreenTriangle();  # 画第二个三角形
    turtle.setheading(0)  # 头向左
    turtle.forward(stepSize)  # 移动指定单位
    draw1GreenTriangle();  # 画第三个三角形
    turtle.forward(stepSize)  # 移动指定个单位


def draw9GreenTriangle():
    """ 就是画九个三角形
    原图片可以看做是3个这样的9个三角形组成的
    """
    draw3GreenTriangle()  # 画第一个三个小三角形
    turtle.left(120)  # 逆时针旋转120度
    turtle.forward(stepSize * 2)  # 移动2个指定单位
    draw3GreenTriangle()  # 画第二个三个小三角形
    turtle.setheading(0)  # 头向左
    turtle.forward(stepSize * 2)  # 移动2个指定单位
    draw3GreenTriangle()  # 画第三个三个小三角形
    turtle.forward(stepSize * 2)  # 移动2个指定单位


def draw27GreenTriangle():
    """ 画出最终图像， 就是27个小三角形，
    其由三个draw9GreenTriangle()的结果组成
    """
    draw9GreenTriangle()
    turtle.left(120)  # 逆时针旋转120度
    turtle.forward(stepSize * 4)  # 移动4个指定单位
    draw9GreenTriangle()
    turtle.setheading(0)  # 头向左
    turtle.forward(stepSize * 4)  # 移动4个指定单位
    draw9GreenTriangle()


if __name__ == "__main__":
    draw27GreenTriangle();
    turtle.mainloop()
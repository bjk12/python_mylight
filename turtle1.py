# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:10:01 2020

@author: BJK
"""
# import turtle as tle

# def go_to(x, y):
#     tle.up()
#     tle.goto(x, y)
#     tle.down()
# def big_Circle(size):  #函数用于绘制心的大圆
#     tle.speed(10)
#     for i in range(150):
#         tle.forward(size)
#         tle.right(0.3)
# def small_Circle(size):  #函数用于绘制心的小圆
#     tle.speed(10)
#     for i in range(210):
#         tle.forward(size)
#         tle.right(0.786)
# def line(size):
#     tle.speed(10)
#     tle.forward(51*size)
# def heart( x, y, size):
#     tle.speed(10)
#     go_to(x, y)
#     tle.left(150)
#     tle.begin_fill()
#     line(size)
#     big_Circle(size)
#     small_Circle(size)
#     tle.left(120)
#     small_Circle(size)
#     big_Circle(size)
#     line(size)
#     tle.end_fill()
# def arrow():
#     tle.pensize(10)
#     tle.setheading(0)
#     go_to(-400, 0)
#     tle.left(15)
#     tle.forward(150)
#     go_to(339, 178)
#     tle.forward(150)
# def arrowHead():
#     tle.pensize(1)
#     tle.speed(10)
#     tle.color('red', 'red')
#     tle.begin_fill()
#     tle.left(120)
#     tle.forward(20)
#     tle.right(150)
#     tle.forward(35)
#     tle.right(120)
#     tle.forward(35)
#     tle.right(150)
#     tle.forward(20)
#     tle.end_fill()
# def main():
#     tle.pensize(2)
#     tle.setup(width=0.8,height=0.6, startx=100, starty=100)
#     tle.color('red', 'pink')
#     tle.delay(0)
#     #tle.getscreen().tracer(30, 0) #取消注释后，快速显示图案
#     heart(200, 0, 1)          #画出第一颗心，前面两个参数控制心的位置，函数最后一个参数可控制心的大小
#     tle.setheading(0)         #使画笔的方向朝向x轴正方向
#     heart(-80, -100, 1.5)     #画出第二颗心
#     arrow()                   #画出穿过两颗心的直线
#     arrowHead()               #画出箭的箭头
#     go_to(400, -300)
#     tle.done()
   
# if __name__ ==  '__main__':
#     main()
# input ("\n\n按回车结束:")


import turtle


turtle.penup()
turtle.right(90)
turtle.bk(200)
turtle.left(90)
turtle.bk(200)
turtle.pendown()

turtle.speed(1)
turtle.delay(3)

turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(10, 180)
turtle.circle(25, 110)
turtle.left(50)
turtle.circle(60, 45)
turtle.circle(20, 170)
turtle.right(24)
turtle.fd(30)
turtle.left(10)
turtle.circle(30, 110)
turtle.fd(20)
turtle.left(40)
turtle.circle(90, 70)
turtle.circle(30, 150)
turtle.right(30)
turtle.fd(15)
turtle.circle(80, 90)
turtle.left(15)
turtle.fd(45)
turtle.right(165)
turtle.fd(20)
turtle.left(155)
turtle.circle(150, 80)
turtle.left(50)
turtle.circle(150, 90)
turtle.end_fill()
# 花瓣1

turtle.left(150)
turtle.circle(-90, 70)
turtle.left(20)
turtle.circle(75, 105)
turtle.setheading(60)
turtle.circle(80, 98)
turtle.circle(-90, 40)

# 花瓣2

turtle.left(180)
turtle.circle(90, 40)
turtle.circle(-80, 98)
turtle.setheading(-83)
# 叶子
turtle.fd(30)
turtle.left(90)
turtle.fd(25)
turtle.left(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(-80, 90)
turtle.right(90)
turtle.circle(-80, 90)
turtle.end_fill()

turtle.right(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(85)
turtle.left(90)
turtle.fd(80)

# 叶子2
turtle.right(90)
turtle.right(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(80, 90)
turtle.left(90)
turtle.circle(80, 90)
turtle.end_fill()

turtle.left(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(60)
turtle.right(90)
turtle.circle(200, 60)

# 文字

printer = turtle.Turtle()
printer.hideturtle()
printer.penup()
printer.right(30)
printer.fd(300)

printer.write("小花送你，请给我你的自拍照(*^▽^*)\n\n", align="right", font=("楷体", 16, "bold"))
printer.write("           from 建康", align="center", font=("楷体", 12, "normal"))

# printer.write("萌妮，happy birthday!\n\n", align="right", font=("楷体", 16, "bold"))
# printer.write("           from 建康", align="center", font=("楷体", 12, "normal"))

turtle.done()
input ("\n\n按回车结束:")

# from turtle import*

# speed(10)
# def nose(x,y):#鼻子
#     penup()#提起笔
#     goto(x,y)#定位
#     pendown()#落笔，开始画
#     setheading(-30)#将乌龟的方向设置为to_angle/为数字（0-东、90-北、180-西、270-南）
#     begin_fill()#准备开始填充图形
#     a=0.4
#     for i in range(120):
#         if 0<=i<30 or 60<=i<90:
#             a=a+0.08
#             left(3) #向左转3度
#             forward(a) #向前走a的步长
#         else:
#             a=a-0.08
#             left(3)
#             forward(a)
#     end_fill()#填充完成
#     penup()
#     setheading(90)
#     forward(25)
#     setheading(0)
#     forward(10)
#     pendown()
#     pencolor(255,155,192)#画笔颜色
#     setheading(10)
#     begin_fill()
#     circle(5)
#     color(160,82,45)#返回或设置pencolor和fillcolor
#     end_fill()
#     penup()
#     setheading(0)
#     forward(20)
#     pendown()
#     pencolor(255,155,192)
#     setheading(10)
#     begin_fill()
#     circle(5)
#     color(160,82,45)
#     end_fill()
# def head(x,y):#头
#     color((255,155,192),"pink")
#     penup()
#     goto(x,y)
#     setheading(0)
#     pendown()
#     begin_fill()
#     setheading(180)
#     circle(300,-30)
#     circle(100,-60)
#     circle(80,-100)
#     circle(150,-20)
#     circle(60,-95)
#     setheading(161)
#     circle(-300,15)
#     penup()
#     goto(-100,100)
#     pendown()
#     setheading(-30)
#     a=0.4
#     for i in range(60):
#         if 0<=i<30 or 60<=i<90:
#             a=a+0.08
#             lt(3) #向左转3度
#             fd(a) #向前走a的步长
#         else:
#             a=a-0.08
#             lt(3)
#             fd(a)
#     end_fill()
# def ears(x,y): #耳朵
#     color((255,155,192),"pink")
#     penup()
#     goto(x,y)
#     pendown()
#     begin_fill()
#     setheading(100)
#     circle(-50,50)
#     circle(-10,120)
#     circle(-50,54)
#     end_fill()
#     penup()
#     setheading(90)
#     forward(-12)
#     setheading(0)
#     forward(30)
#     pendown()
#     begin_fill()
#     setheading(100)
#     circle(-50,50)
#     circle(-10,120)
#     circle(-50,56)
#     end_fill()
# def eyes(x,y):#眼睛
#     color((255,155,192),"white")
#     penup()
#     setheading(90)
#     forward(-20)
#     setheading(0)
#     forward(-95)
#     pendown()
#     begin_fill()
#     circle(15)
#     end_fill()
#     color("black")
#     penup()
#     setheading(90)
#     forward(12)
#     setheading(0)
#     forward(-3)
#     pendown()
#     begin_fill()
#     circle(3)
#     end_fill()
#     color((255,155,192),"white")
#     penup()
#     seth(90)
#     forward(-25)
#     seth(0)
#     forward(40)
#     pendown()
#     begin_fill()
#     circle(15)
#     end_fill()
#     color("black")
#     penup()
#     setheading(90)
#     forward(12)
#     setheading(0)
#     forward(-3)
#     pendown()
#     begin_fill()
#     circle(3)
#     end_fill()
# def cheek(x,y):#腮
#     color((255,155,192))
#     penup()
#     goto(x,y)
#     pendown()
#     setheading(0)
#     begin_fill()
#     circle(30)
#     end_fill()
# def mouth(x,y): #嘴
#     color(239,69,19)
#     penup()
#     goto(x,y)
#     pendown()
#     setheading(-80)
#     circle(30,40)
#     circle(40,80)
# def body(x,y):#身体
#     color("red",(255,99,71))
#     penup()
#     goto(x,y)
#     pendown()
#     begin_fill()
#     setheading(-130)
#     circle(100,10)
#     circle(300,30)
#     setheading(0)
#     forward(230)
#     setheading(90)
#     circle(300,30)
#     circle(100,3)
#     color((255,155,192),(255,100,100))
#     setheading(-135)
#     circle(-80,63)
#     circle(-150,24)
#     end_fill()
# def hands(x,y):#手
#     color((255,155,192))
#     penup()
#     goto(x,y)
#     pendown()
#     setheading(-160)
#     circle(300,15)
#     penup()
#     setheading(90)
#     forward(15)
#     setheading(0)
#     forward(0)
#     pendown()
#     setheading(-10)
#     circle(-20,90)
#     penup()
#     setheading(90)
#     forward(30)
#     setheading(0)
#     forward(237)
#     pendown()
#     setheading(-20)
#     circle(-300,15)
#     penup()
#     setheading(90)
#     forward(20)
#     setheading(0)
#     forward(0)
#     pendown()
#     setheading(-170)
#     circle(20,90)
# def foot(x,y):#脚
#     pensize(10)
#     color((240,128,128))
#     penup()
#     goto(x,y)
#     pendown()
#     setheading(-90)
#     forward(40)
#     setheading(-180)
#     color("black")
#     pensize(15)
#     fd(20)
#     pensize(10)
#     color((240,128,128))
#     penup()
#     setheading(90)
#     forward(40)
#     setheading(0)
#     forward(90)
#     pendown()
#     setheading(-90)
#     forward(40)
#     setheading(-180)
#     color("black")
#     pensize(15)
#     fd(20)
# def tail(x,y):#尾巴
#     pensize(4)
#     color((255,155,192))
#     penup()
#     goto(x,y)
#     pendown()
#     seth(0)
#     circle(70,20)
#     circle(10,330)
#     circle(70,30)
# def setting():          #参数设置
#     speed(99)
#     pensize(4)
#     hideturtle()        #使乌龟无形（隐藏）
#     colormode(255)      #将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内
#     color((255,155,192),"pink")
#     setup(840,500)
# def main():
#     setting()           #画布、画笔设置
#     nose(-100,100)      #鼻子
#     head(-69,167)       #头
#     ears(0,160)         #耳朵
#     eyes(0,140)         #眼睛
#     cheek(80,10)        #腮
#     mouth(-20,30)       #嘴
#     body(-32,-8)        #身体
#     hands(-56,-45)      #手
#     foot(2,-177)        #脚
#     tail(148,-155)      #尾巴
#     done()

# if __name__ == '__main__':
# 	main()
# input ("\n\n按回车结束:")




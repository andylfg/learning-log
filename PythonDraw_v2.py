#PythonDraw.py
import turtle

turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40) #顺时针旋转40度
#第一个参数表示半径，默认角度是360度，在海龟当前位置开始画圆
#半径为正数圆心在海龟左侧，按逆时针画圆，半径为负数圆心在海龟右侧，按顺时针画圆
for i in range(4):
    turtle.circle(40, 80) 
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()

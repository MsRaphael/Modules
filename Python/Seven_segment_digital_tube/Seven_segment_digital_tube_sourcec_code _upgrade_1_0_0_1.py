#codinh:utf-8
#此模块使用Notpad++编辑，请使用Notpad++获取最佳阅读效果
#这是一个基于python的7段数码管模块，您可以调用此模块来实现不同的数字显示
#此模块也可用于绘制年份


import turtle

#画七段数码管的一个管
def drawLine(draw):
	turtle.pendown() if draw else turtle.penup()
	turtle.fd(40)
	turtle.right(90)

#画一个数字
def drawDigit(digit):
	drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
	drawLine(True) if digit in [0,1,4,3,5,6,7,8,9] else drawLine(False)
	drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
	drawLine(True) if digit in [0,2,6,8] else drawLine(False)
	turtle.left(90)
	drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
	drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
	drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
	turtle.left(180)

#画几个数码管
def drawDate(date,spacing):
	for i in date:
		drawDigit(eval(i))
		turtle.penup()
		turtle.fd(spacing)

#调用函数

def ssdt(year,month=0,day=0,n=1,p_size=10,p_color='red',c_space=25):
	turtle.pensize(p_size)
	turtle.pencolor(p_color)
	year=str(year)
	for i in year:
		drawDigit(eval(i))
		turtle.penup()
		turtle.fd(c_space)
	if n==2:
		month=str(month)
		turtle.penup()
		turtle.fd(c_space)
		for i2 in month:
			drawDigit(eval(i2))
			turtle.penup()
			turtle.fd(c_space)
	elif n==3:
		month=str(month)
		turtle.penup()
		turtle.fd(c_space)
		for i2 in month:
			drawDigit(eval(i2))
			turtle.penup()
			turtle.fd(c_space)
		day=str(day)
		turtle.penup()
		turtle.fd(c_space)
		for i3 in day:
			drawDigit(eval(i3))
			turtle.penup()
			turtle.fd(c_space)

def drawGap(space):
	turtle.penup()
	turtle.fd(space)
def drawLinePro(draw,space=5,size=35):
	drawGap(space)
	turtle.pendown() if draw else turtle.penup()
	turtle.fd(size)
	drawGap(space)
	turtle.right(90)
def drawDigitPro(digit,space=5,size=35):
	drawLinePro(True,space,size) if digit in [2,3,4,5,8,9] else drawLinePro(False,space,size)
	drawLinePro(True,space,size) if digit in [0,1,3,4,5,6,7,8,9] else drawLinePro(False,space,size)
	drawLinePro(True,space,size) if digit in [0,2,3,5,6,8,9] else drawLinePro(False,space,size)
	drawLinePro(True,space,size) if digit in [0,2,6,8] else drawLinePro(False,space,size)
	turtle.left(90)
	drawLinePro(True,space,size) if digit in [0,4,5,6,8,9] else drawLinePro(False,space,size)
	drawLinePro(True,space,size) if digit in [0,2,3,5,6,7,8,9] else drawLinePro(False,space,size)
	drawLinePro(True,space,size) if digit in [0,1,2,3,4,7,8,9] else drawLinePro(False,space,size)

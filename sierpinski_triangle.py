import turtle
from random import *

def draw():
	playground = turtle.Screen()
	playground.bgcolor("white")
	playground.screensize(2000, 2000)
	playground.title("Sierpinski Triangle")
	trtl = turtle.Turtle()              
	trtl.color("black")
	trtl.speed(0)
	trtl.dot()
	trtl.penup()
	trtl.forward(800)
	trtl.pendown()
	trtl.dot()
	point1 = trtl.pos()             
	trtl.penup()
	trtl.left(120)
	trtl.forward(800)
	trtl.pendown()
	trtl.dot()
	point2 = trtl.pos()        
	trtl.penup()
	trtl.left(120)
	trtl.forward(800)
	trtl.pendown()
	trtl.dot()
	point3 = trtl.pos()       
	trtl.penup()
	trtl.right(240)
	trtl.forward(400)
	trtl.left(90)
	trtl.forward(86.6025403784)
	trtl.dot()

	i = 0
	while i < 10000:
		current_point = trtl.pos() 
		current_x = current_point[0]
		current_y = current_point[1]
		x = int
		ran = random()
		if ran <= .33:
			x = 1
		elif ran <= .66:
			x = 2
		else:
			x = 3
		
		if x == 1:
			x = (current_x+point1[0])/2
			y = (current_y+point1[1])/2
			trtl.goto(x, y)
			trtl.pendown()
			trtl.color("green")
			trtl.dot()
		elif x == 2:
			x = (current_x+point2[0])/2
			y = (current_y+point2[1])/2
			trtl.goto(x, y)
			trtl.pendown()
			trtl.color("red")
			trtl.dot()
		elif x == 3:
			x = (current_x+point3[0])/2
			y = (current_y+point3[1])/2
			trtl.goto(x, y)
			trtl.pendown()
			trtl.color("blue")
			trtl.dot()
		i+=1
		trtl.penup()
	playground.exitonclick()  

draw()
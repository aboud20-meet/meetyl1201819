
from turtle import Turtle
import turtle
'''

class Square(Turtle):
	def __init__ (self, size, color):
		Turtle.__init__ (self)
		self.Shapesize(size)

import turtle
import random 

def change_color():
    	R = random.random()
    	B = random.random()
    	G = random.random()

    	turtle.color(R, G, B)

def turn_and_change_color(x, y):
    turtle.left(10)
    change_color()

turtle.onscreenclick(turn_and_change_color)

def move_forward():
    turtle.forward(1)
    turtle.ontimer(move_forward, 25)

move_forward()

turtle.mainloop()
'''
class Hexagon(Turtle):
    def __init__ (self, size, color):
        Turtle.__init__(self)

        turtle.home()
        turtle.begin_poly()
        i = 6
        turtle.pu()
    f.color(color)
    self.speed(speed)
# Code to create two ball objects here

def check_collision(ball1, ball2):
    #logic to check if the ballf.color(color)
    self.speed(speed)
# Code to create two ball objects here

def check_collision(ball1, ball2):
    #logic to check if the ball    for i in range(6):
            turtle.fd(size)
            turtle.left(60)

        turtle.end_poly()
        hexagon = turtle.get_poly()
        turtle.register_shape("hexagon", hexagon)

        self.color(color)
        self.shape("hexagon")


h = Hexagon(400, "red")





turtle.mainloop()


 		
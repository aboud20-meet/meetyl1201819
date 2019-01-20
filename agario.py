import turtle 
import time 
import random 
from ball import Ball 
import math

turtle.tracer(0)
turtle.hideturtle()
RUNNING = True 
SLEEP = 0.0077
screen_width = turtle.getcanvas().winfo_width()/2
screen_hieght = turtle.getcanvas().winfo_height()/2
MY_BALL= Ball (10, 100, 1, 1, 10, "blue")
number_of_balls= 5
minimum_ball_radius= 10
maximum_ball_radius= 100
minimum_ball_dx= -5
maximum_ball_dx= 5
minimum_ball_dy= -5
maximum_ball_dy= 5
BALLS = []
for i in range (number_of_balls):
	x = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
	y = random.randint(-screen_hieght + maximum_ball_radius, screen_hieght - maximum_ball_radius)
	dx = random.randint(minimum_ball_dx, maximum_ball_dx)
	dy = random.randint(minimum_ball_dy, maximum_ball_dy)
	radius = random.randint(minimum_ball_radius, maximum_ball_radius)
	color = (random.random(), random.random(), random.random())
	if dx == 0:
		dx= random.randint(minimum_ball_dx, maximum_ball_dx)
	if dy == 0:
		dy = random.randint(minimum_ball_dy, maximum_ball_dy)
	new_ball=Ball(x,y,dx,dy,radius,color)
	BALLS.append(new_ball)

def move_all_balls():
	for b in BALLS : 
		b.move(SCREEN_WIDTH, SCREEN_HIEGHT)


def collide (ball_a, ball_b):
	if ball_a == ball_b:
		return False
		


import turtle 
from turtle import * 

class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self) 
		self.x=x
		self.y=y
		self.dx=dx
		self.dy=dy
		self.r=r
		self.color(color)
		self.shape("circle")
		self.goto(x,y)
		self.shapesize(r/10)
	def move(self, screen_width, screen_height):
		current_x = xcor()
		new_x = current_x + self.dx 
		current_y = ycor()
		new_y = current_y + self.dy 
		right_side_ball = new_x + self.r 
		left_side_ball = new_x - self.r 
		upper_side_ball = new_y + self.r 
		bottom_side_ball = new_y - self.r 
		self.goto(new_x, new_y)
		if new_x >= screen_width or new_x <= screen_width: 
			self.dx = self.dx

		if new_y >= screen_hieght or new_y <= screen_hieght:
			self.dx = self.dx 



# ball = Ball(0, 0, 1, 1, 10,"blue")
# turtle.mainloop()







 



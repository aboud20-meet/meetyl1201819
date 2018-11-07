print ("aboud")
name = "aboud"
print (name*2)
print ("aboud"*3)
print ("aboud"*3)
print ("aboud"*100)
number1 = 30
print (number1)
number2 = 15
print (number2)
ls = [1, 2, 4]
for i in ls:
	print i 
	print i*2
b = sum(ls)
print (b) 
import turtle
turtle.begin_fill()
turtle.goto (0,100)
turtle.goto (100,100)
turtle.goto (100,0)
turtle.goto (0,0)
turtle.end_fill()
turtle.penup ()
turtle.goto (0,-100)
turtle.pendown ()
turtle.begin_fill ()
turtle.fillcolor("blue")
turtle.circle(500)
turtle.end_fill()
turtle.mainloop()
import turtle
import random 

def fib_word(n):
	fib_word_0 = "0"
	fib_word_1 = "01"
	
	word = ""
	
	for i in range (2,n+1):
		word = fib_word_1 + fib_word_0
		fib_word_0 = fib_word_1
		fib_word_1 = word
	return word

canvas = turtle.Screen()
canvas.bgcolor('black')
canvas.setup(width = 800, height = 800)
turtle.penup()
turtle.setpos(-200,-400)
turtle.speed(0)
turtle.pendown()	
	
word=fib_word(21)
canvas.tracer(0)

for k, digit in enumerate(word):
	turtle.color( random.uniform(0,1), random.uniform(0,1), random.uniform(0,1) )
	turtle.forward(1)
	if digit == "0":
		if k%2 == 0:
			turtle.left(90)
		else:
			turtle.right(90)
canvas.update()
turtle.exitonclick()

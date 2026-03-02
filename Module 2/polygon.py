import time
import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(400,600)
hexagon = turtle.Turtle()
for i in range(0,6):
  turtle.forward(50)
  turtle.right(60)
  
  time.sleep(1)
turtle.done()
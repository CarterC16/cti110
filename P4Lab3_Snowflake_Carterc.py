# 10/27/2018
# CTI-110 P4Lab3 SnowFlake
# Christian Carter

import turtle
import random

# setup the window with a background colour
wn = turtle.Screen()
wn.bgcolor("lightblue")

# assign a name to your turtle
elsa = turtle.Turtle()
elsa.speed(23)

# create a list of colours
sfcolor = ["white", "cyan", "purple", "yellow"]

# create a function to create different size snowflakes
def snowflake(size):
# move the pen into starting position
    elsa.penup()
    elsa.forward(10*size)
    elsa.left(45)
    elsa.pendown()
    elsa.color(random.choice(sfcolor))
    # draw branch 8 times to make a snowflake
    for i in range(8):
        branch(size)   
        elsa.left(45)
    

# create one branch of the snowflake
def branch(size):
    for i in range(3):
        for i in range(3):
            elsa.forward(10.0*size/3)
            elsa.backward(10.0*size/3)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(10.0*size/3)
        elsa.left(45)
    elsa.right(90) 
    elsa.forward(10.0*size)

# loop to create 20 different sized snowflakes with different starting co-ordinates
for i in range(20):
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    sf_size = random.randint(3, 10)
    elsa.penup()
    elsa.goto(x, y)
    elsa.pendown()
    snowflake(sf_size)

# leave the window open until you click to close  
wn.exitonclick() 

# 10/25/2018
# CTI-110 P4Lab1: Shapes
# Christian Carter
import turtle             # Allows us to use turtles
win = turtle.Screen()      # Creates a playground for turtles
t = turtle.Turtle()    # Create a turtle, assign to t

# commands from here to the last line can be replaced
# turn the other direction, so the triangle's on the outside
for i in (1,2,3):
    for j in (1,2):
        t.forward(50)          
        t.left(90)             
        t.forward(50)
        t.left(90)
        t.forward(50)
    t.left(90)
    t.forward(50)

# add some display options
t.pensize(3)            # increase pensize (takes integer)
t.pencolor("purple")     # set pencolor (takes string)
t.shape("turtle")

# triangle, sides are 360 / 3 = 120 degrees
# turn the other direction, so the triangle's on the outside
for i in (1,2,3):
    for j in (1,2):
        t.forward(100)          
        t.left(120)            
    t.forward(100)
    t.left(120)
    t.forward(100)

# end commands
win.mainloop()             # Wait for user to close window


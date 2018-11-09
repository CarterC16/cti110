# 10/25/2018
# CTI-110 P4Lab2 Initials
# Christian Carter

import turtle
win = turtle.Screen()
t = turtle.Turtle()

# display options
t.pensize(6)
t.pencolor("Green")
t.shape("turtle")
t.write("C C",move=True,align="center",font=("Times New Roman",50,"normal"))
t.forward(1)
t.circle(-100,-200,50)


t.right(150)
t.forward(80)
t.circle(-100,50)
t.circle(-80,-200,50)


# end commands
win.mainloop()  

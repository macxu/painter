
import turtle

pen = turtle.Turtle()
pen.hideturtle()

pen.fillcolor('red')
pen.begin_fill()

pen.up()
pen.down()

# set the starting direction
pen.left(110)

# draw the left bottom part
while pen.heading() < 140:
    # rotate & forward
    pen.left(1)
    pen.forward(2)

# move up
pen.forward(90)

# draw the left upper part
while pen.xcor() < 0:
    pen.right(0.8)
    pen.forward(1)

# go back to the starting point, and do the right part as a mirror
pen.up()
pen.goto(0, 0)
pen.down()

# set the direction
pen.setheading(70)

# draw the right bottom part
while pen.heading() > 40:
    # Defining step by step curve motion
    pen.right(1)
    pen.forward(2)

# move up
pen.forward(90)

# draw the right upper part
while pen.xcor() > 0:
    print(pen.xcor())
    pen.left(0.8)
    pen.forward(1)

# Ending the filling of the color
pen.end_fill()

pen.up()
pen.down()

pen.ht()
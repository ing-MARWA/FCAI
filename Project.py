import turtle as t
import graphics as g
import time
an=t.Screen()
t.ht()
t.penup()
t.speed(100)
an.bgcolor("gray1")
t.shape("turtle")
t.color("black")

import turtle

def tree(branchLen,t):
    t.pensize(5)
    if branchLen > 10:
        t.forward(branchLen)
        t.right(40)
        tree(branchLen-15,t)
        t.left(80)
        tree(branchLen-15,t)
        t.right(40)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.color("darkorchid3")
    tree(100,t)
    #myWin.exitonclick()

main()
#drawing letter F

t.penup()
t.setpos(-350,160)
t.pendown()
t.pensize(10)
t.pencolor("deeppink1")
t.forward(100)
t.backward(100)
t.right(90)
t.forward(100)
t.pencolor("royalblue2")
t.left(90)
t.forward(100)
t.backward(100)
t.right(90)
t.forward(100)
#drawing letter C
t.penup()
t.pencolor("chartreuse1")
t.backward(200)
t.right(-90)
t.forward(100)
t.right(90)
t.forward(180)
t.right(-90)
t.forward(150)
t.pendown()
t.pensize(10)
t.circle(100,-185)
#drawing letter A
t.penup()
t.right(-185)
t.forward(140)
t.pendown()
t.pensize(10)
t.pencolor("royalblue2")
t.right(60)
t.forward(230)
t.backward(200)
t.pencolor("gold1")
t.left(-60)
t.forward(200)
t.backward(85)
t.left(120)
t.forward(105)
#drawing robot
t.ht()
t.penup()
t.speed("fast")
def rectangle(horizontal, vertical, color):
    t.pendown()  # Put's the turtle pen to start drawing
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):  # using the range(1, 3) makes the loop run twice
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()  # put's the pen back to stop drawing
    t.penup()  # Pull the pen back up
    t.speed('slow')  # set's the turtle speed

# Feet
t.goto(185, -50)  # Move the turtle position x = -100 and y = 150
rectangle(40, 10, 'blue2')  # We use the rectangle function to draw a blue rect 50 wide and 20 high
t.goto(235, -50)
rectangle(40, 10, 'blue2')
# legs
t.goto(210,0)  # the turtle moves to position x = 210, y = 0
rectangle(10, 50, 'mintcream')  # Draws the left leg
t.goto(250,0)
rectangle(-10, 50, 'mintcream')  # Draws the Right leg
# body
t.goto(190,100)
rectangle(80, 100, 'blue2')
# arms
t.goto(140, 70)
rectangle(50, 7, 'mintcream')  # Upper right arm
t.goto(140, 85)
rectangle(10, 20, 'mintcream')  # lower right arm
t.goto(270, 70)
rectangle(50, 7, 'mintcream')  # Upper left arm
t.goto(310, 85)
rectangle(10, 20, 'mintcream')  # Lower left arm
# Neck
t.goto(220,115)
rectangle(15, 15, 'mintcream')
# Head
t.goto(200,145)
rectangle(60,30, 'blue2')
# Eyes
#t.goto(215,140)
#rectangle(30,5, 'white')  # White part of the eye
t.goto(220,135)
t.dot(12,'black')  # Draw the Right Pupil
t.dot(7,"mintcream")
t.goto(238, 135)
t.dot(12,'black')  # Draw the left pupil
t.dot(7,"mintcream")
# Mouth
t.goto(210, 123)
rectangle(38,3, 'mintcream')

t.hideturtle()  # This will make the turtle invisible
for i in range(50):
    an.bgcolor("#cce6ff")
    an.bgcolor("#0086b3")
    an.bgcolor("#4dffff")
    an.bgcolor("#6b00b3")
    time.sleep(1)

t.home()

turtle.exitonclick()

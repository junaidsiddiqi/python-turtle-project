import turtle
import random
import os
os.system("cls")

# To make it a little fun to play around with

def impostor_check(player_name):
    checker = random.randint(0,1)

    if checker == 0:
        return f"{player_name} was The Impostor."
    elif checker == 1:
        return f"{player_name} was not The Impostor."

name = input("EMERGENCY MEETING! Who are we voting out? ")
wn = turtle.Screen()
space = turtle.Turtle()
t = turtle.Turtle()
f = turtle.Turtle()
wn.bgcolor("black")
space.color("white")
space.speed(0)
t.speed(0)
t.hideturtle()
space.hideturtle()
f.hideturtle()

# function to make stars for background
def createStar(x,y):
    space.penup()
    space.goto(x,y)
    space.pendown()
    size = random.randint(1,3)
    space.begin_fill()
    space.circle(size)
    space.end_fill()

# inserts stars into background
for i in range(200):
    x = random.randint(-1000,1000)
    y = random.randint(-1000,1000)
    createStar(x,y)

t.penup()
t.goto(500,75)
t.right(135)
t.pendown()

def body():
    t.pensize(20)
    t.fillcolor("red")
    t.begin_fill()

    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)

    t.right(180)
    t.circle(100, -180)

    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)

    t.circle(40, -180)

    t.left(7)
    t.backward(50)

    t.penup()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pendown()
    t.right(240)
    t.circle(50, -70)

    t.end_fill()


# this is the visor part of the figure
def visor():
    t.penup()
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)

    t.pendown()
    t.fillcolor("skyblue")
    t.begin_fill()

    t.right(150)
    t.circle(90, -55)

    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)
        
    
    t.circle(50, -190)
    t.right(170)
    t.forward(80)

    t.right(180)
    t.circle(45, -30)

    t.end_fill()

# this is its backpack
def backpack():
    t.penup()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)

    t.fillcolor("red")
    t.begin_fill()

    t.pendown()
    t.forward(30)
    t.right(255)

    t.circle(300, -30)
    t.right(260)
    t.forward(30)

    t.end_fill()

body()
visor()
backpack()

f.penup()
f.goto(-200, 0)
f.pendown()
f.color("white")
result = impostor_check(name)
print(result)
f.write(result, font=("Arial", 24, "normal"))


wn.exitonclick()

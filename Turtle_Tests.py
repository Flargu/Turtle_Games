import turtle
import random

yes=turtle.Turtle(shape="circle")
yes.goto(-50,-50)
t=turtle.Turtle(shape="turtle")
print(t)
print(t.getturtle())
t.fillcolor("dark green")
t.penup()
t.goto(-200,100)
a=turtle.Turtle()
a.penup()
a.goto(-200,150)
def walk():
    t.fd(1)
def walk_back():
    t.bk(1)
def turn_right():
    t.rt(45)
def turn_left():
    t.rt(-45)
turtle.onkeypress(walk,"Up")
turtle.onkeypress(walk_back,"s")
turtle.onkeypress(turn_right,"d")
turtle.onkeypress(turn_left,"a")
def timer_a():
    a.fd(400) 
turtle.ontimer(timer_a,1)
turtle.fd(200)
turtle.rt(90)
turtle.fd(200)
turtle.penup()
turtle.home()
def turtles2(n):
    a={}
    x=50
    for i in range(n):
        key=f"turtle{i}"
        a[key]=turtle.Turtle()
        a[key].shape("turtle")
        a[key].rt(90)
        a[key].fd(x)
        x=x+50

def run_forrest_run(forrest,jenny):
    forrest=turtle.Turtle(shape="turtle")
    forrest.speed(0)
    def forrest_runs(x,y):
        forrest.fd(5)
    jenny.onclick(forrest_runs)
    return forrest
clicker=turtle.Turtle()
#clicker.resizemode("user")
#clicker.turtlesize(5,5,5)
runner=turtle.Turtle()
print(runner.fillcolor())
runner.fillcolor("blue")
#turtle.colormode(cmode=255)
print(runner.fillcolor())
#runner.fillcolor(24,5,200)
print(runner.fillcolor())
run_forrest_run(runner,clicker)
turtles2(4)
bob=turtle.Turtle()
bob.fillcolor("violet")
bob.fillcolor("green")
turtle.colormode(cmode=255)
turtle.colormode(255)
bob.fillcolor(random.sample(range(0,255),3))
bob.fillcolor([201, 89, 163])
bob.fd(200)
bob.fillcolor(list(random.sample(range(0,255),3)))
bob.rt(90)
bob.fd(100)
mike=turtle.Turtle()
petra=turtle.Turtle()
mike.penup()
petra.penup()
mike.goto(-350,200)
petra.goto(-350,250)
mike.speed(1)
petra.speed(1)
print(turtle.delay())
turtle.delay(0)
print(turtle.delay())
for i in range(500):
    turtle.delay(0)
    petra.fd(1)
    turtle.delay(0)
    mike.fd(1)

print("done")
turtle.clearscreen()
clicker=turtle.Turtle()
clicker.goto(50,50)
run_forrest_run(bob,clicker)
bob.fd(100)

turtle.mainloop()
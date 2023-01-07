import turtle
def shape(x,y,a,p):
    turtle.ht()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(p):
        turtle.fd(a)
        turtle.rt(360/p)
    turtle.penup()
def fullshape(x,y,a,p):
    turtle.ht()
    turtle.begin_fill()
    shape(x,y,a,p)
    turtle.end_fill()
def squareline(start,x,y,n,a):
    p=4
    if start=='full':
        for i in range(int(n/2)):
            fullshape(x,y,a,p)
            x=x+a
            shape(x,y,a,p)
            x=x+a
    elif start=='empty':
        for i in range(int(n/2)):
            shape(x,y,a,p)
            x=x+a
            fullshape(x,y,a,p)
            x=x+a
def finishflag(x,y,l,b,a):
    turtle.speed(0)
    turtle.delay(0)
    start='full'
    for i in range(l):
        xnew=x
        squareline(start,xnew,y,b,a)
        y=y-a
        if start=='full':
            start='empty'
        elif start=='empty':
            start='full'
    turtle.penup()
    turtle.home()
runner=turtle.Turtle(shape='turtle')
finish_x1=200
finish_y1=200
finish_l=10
finish_nsq=10
finish_sq=10
track_width=finish_nsq*finish_sq
finish_x2=finish_x1+finish_nsq*finish_sq
finish_y2=finish_y1-finish_l*finish_sq
start_x1=-finish_x1
start_y1=finish_y1
start_x2=start_x1+track_width
start_y2=finish_y2
track_l_out=(-2)*start_x1+track_width
track_l_in=(-2)*start_x2+track_width
finishflag(finish_x1,finish_y1,finish_l,finish_nsq,finish_sq)
shape(start_x1,start_y1,track_l_out,4)
shape(start_x2,start_y2,track_l_in,4)
def forward():
    runner.fd(5)
def go_left():
    runner.lt(10)
def go_right():
    runner.rt(10)
def finish_pole(x,y):
    turtle.delay(0)
    finish=turtle.Turtle(shape='circle')
    finish.speed(0)
    finish.penup()
    finish.goto(x,y)
    return finish
runner.speed(1)
runner.penup()
runner.goto(-200,-200)
turtle.onkey(forward,'Up')
#finish_up=finish_pole(200,200)
#finish_down=finish_pole(200,150)
turtle_width = 20
limit_left_out = start_x1
limit_right_out = finish_x2
limit_up_out = finish_y1
limit_down_out = finish_y1-track_l_out
limit_left_in = start_x2
limit_right_in = finish_x1
limit_up_in = start_y2
limit_down_in = start_y2-track_l_in

limit_left_out_turtle = limit_left_out+ turtle_width/2
limit_right_out_turtle = limit_right_out - turtle_width/2
limit_up_out_turtle = limit_up_out - turtle_width/2
limit_down_out_turtle = limit_down_out + turtle_width/2
limit_left_in_turtle = limit_left_in - turtle_width/2
limit_right_in_turtle = limit_right_in + turtle_width/2
limit_up_in_turtle = limit_up_in + turtle_width/2
limit_down_in_turtle = limit_down_in - turtle_width/2

turtle.onkey(go_left,'Left')
turtle.onkey(go_right,'Right')
turtle.listen()
while True:
    turtle.delay(1)
    runner.fd(1)
    if runner.xcor()<limit_left_out_turtle:
        runner.goto(limit_left_out_turtle,runner.ycor())
    if runner.xcor()>limit_right_out_turtle:
        runner.goto(limit_right_out_turtle,runner.ycor())
    if runner.ycor()>limit_up_out_turtle:
        runner.goto(runner.xcor(),limit_up_out_turtle)
    if runner.ycor()<limit_down_out_turtle:
        runner.goto(runner.xcor(),limit_down_out_turtle)
    
    if runner.xcor()>limit_left_in_turtle and runner.xcor()<limit_left_in and runner.ycor()>limit_down_in and runner.ycor()<limit_up_in:
        runner.goto(limit_left_in_turtle,runner.ycor())
    if runner.xcor()<limit_right_in_turtle and runner.xcor()>limit_right_in and runner.ycor()>limit_down_in and runner.ycor()<limit_up_in:
        runner.goto(limit_right_in_turtle,runner.ycor())
    if runner.ycor()<limit_up_in_turtle and runner.ycor()>limit_up_in and runner.xcor()>limit_left_in and runner.xcor()<limit_right_in:
        runner.goto(runner.xcor(),limit_up_in_turtle) 
    if runner.ycor()>limit_down_in_turtle and runner.ycor()<limit_down_in and runner.xcor()>limit_left_in and runner.xcor()<limit_right_in:
        runner.goto(runner.xcor(),limit_down_in_turtle)
       

    if runner.xcor()<finish_x2 and runner.xcor()>finish_x1 and runner.ycor()<finish_y1 and runner.ycor()>finish_y2:
        break
    #if finish
    #runner.stamp()
turtle.mainloop()
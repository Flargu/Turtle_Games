import random
import turtle
turtle.delay(0)
turtle.speed(0)
turtle.colormode(cmode=255)
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
    start='full'
    for i in range(l):
        xnew=x
        squareline(start,xnew,y,b,a)
        y=y-a
        if start=='full':
            start='empty'
        elif start=='empty':
            start='full'
def turtle_tracks(n,p,tw,s,l):
    turtle.ht()
    for i in range (n+1):
        turtle.penup()
        turtle.goto(s,p)
        turtle.pendown()
        turtle.fd(l)
        p=p-tw
def start_line(x,y,l):
    turtle.ht()
    turtle.penup()
    turtle.goto(x,y)
    turtle.rt(90)
    turtle.pendown()
    turtle.fd(l)
def start_race(ax,ay,ts):
    starter=turtle.Turtle(visible=False)
    starter.penup()
    starter.resizemode("user")
    starter.shapesize(ts*5,ts*5,ts*5)
    starter.speed(1)
    starter.goto(ax,ay)
    starter.color("green")
    starter.st()
    def start_signal(x,y):
        turtle.delay(0)
        starter.clear()
        starter.ht()
    turtle.delay(300)
    while starter.isvisible()==True:
        starter.onclick(start_signal)
        starter.color("black")
        starter.color("green")
def race(n,l):
    xwin=1500
    ywin=xwin/2
    tw=24
    b=4
    ax=0
    ay=0
    lt=l+3*tw
    s=-(lt/2)+tw
    fin=lt/2-2*tw
    y=tw*(n/2)
    yr=y-(tw/2)
    sq=tw/b
    ls=n*tw
    lf=int(n*tw/sq)
    st=s-tw
    xworld_base=l+b*tw+tw
    yworld_base=n*tw+tw
    if (xworld_base/xwin)>(yworld_base/ywin):
        xworld=xworld_base
        C_yworld=(xworld/xwin)-(yworld_base/ywin)
        yworld=yworld_base+C_yworld*ywin
    elif (xworld_base/xwin)<(yworld_base/ywin):
        yworld=yworld_base
        C_xworld=(yworld/ywin)-(xworld_base/xwin)
        xworld=xworld_base+C_xworld*xwin
    elif (xworld_base/xwin)==(yworld_base/ywin):
        xworld=xworld_base
        yworld=yworld_base
    ts=xwin/xworld
    turtle.setup(xwin,ywin,0,0)
    turtle.setworldcoordinates(-xworld/2,-yworld/2,xworld/2,yworld/2)
    turtle.tracer(n=0, delay=None)
    turtle_tracks(n,y,tw,st,lt)
    start_line(s,y,ls)
    finishflag(fin,y,lf,b,sq)
    turtle.tracer(n=1, delay=None)
    a={}
    turtle.delay(1)
    for i in range(1,n+1):
        key=f"turtle{i}"
        a[key]=turtle.Turtle(shape="turtle",visible=False)
        a[key].ht()
        a[key].speed(6)
        a[key].shapesize(1,1,0)
        a[key].fillcolor(random.sample(range(0,255),3))
        a[key].penup()
        a[key].goto(s,yr)
        a[key].speed(1)
        a[key].st()
        a[key].turtlesize(ts,ts,0)
        yr=yr-tw
    start_race(ax,ay,ts)
    turtle.delay(1)
    k=list(range(1,n+1))
    z=len(k)
    while z>0:
        t=random.choice(k)
        key=f"turtle{t}"
        a[key].fd(1.5)
        if a[key].xcor()>=fin:
            a[key].fd(1.1*tw)
            k.remove(t)
            z=len(k)
            #a[key].write(str(n-z)+".",move=False, align="center", font=("Arial", 10, "bold"))


race(4,1000)


turtle.mainloop()
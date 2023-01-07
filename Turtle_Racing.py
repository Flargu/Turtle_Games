import random
import time
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
def turtle_tracks(n,p,tw,s,l):
    turtle.ht()
    for i in range (n+1):
        turtle.penup()
        turtle.goto(s,p)
        turtle.pendown()
        turtle.fd(l)
        p=p-tw
    turtle.penup()
    turtle.home()
def start_line(x,y,l):
    turtle.ht()
    turtle.penup()
    turtle.goto(x,y)
    turtle.rt(90)
    turtle.pendown()
    turtle.fd(l)
    turtle.penup()
    turtle.home()
def start_race(ax,ay,ts):
    starter=turtle.Turtle(visible=False)
    starter.penup()
    starter.resizemode("user")
    starter.shapesize(ts*5,ts*5,ts*5)
    starter.speed(0)
    starter.goto(ax,ay)
    starter.color("green")
    starter.st()
    def start_signal(x,y):
        turtle.delay(0)
        starter.clear()
        starter.ht()
    turtle.delay(300)
    starter.onclick(start_signal)
    while starter.isvisible()==True:
        starter.color("black")
        starter.color("green")
def run_forrest_run(forrest,jenny):
    def forrest_runs(x,y):
        turtle.delay(0)
        forrest.fd(4)
        jenny.fillcolor("green")
    def forrest_stops(x,y):
        jenny.fillcolor("red")
    jenny.onclick(forrest_runs)
    jenny.onrelease(forrest_stops)
def world_scale(xwin,ywin,xworld_base,yworld_base):
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
    return xworld,yworld,ts
def race(turtle_name,racer_color,n,l,difficulty):
    turtle.colormode(cmode=255)
    turtle.delay(0)
    turtle.speed(0)
    xwin=1500
    ywin=xwin/2
    tw=24
    b=4
    ntot=n+1
    lt=l+3*tw
    s=-(lt/2)+tw
    fin=lt/2-2*tw
    y=tw*ntot
    yr=y-(tw/2)
    ax=0
    ay=y+2*tw
    y_title=ay+1.5*tw
    sq=tw/b
    ls=ntot*tw
    lf=int(ntot*b)
    st=s-tw
    xworld_base=lt+tw
    yworld_base=y_title+2*tw
    xworld,yworld,ts=world_scale(xwin,ywin,xworld_base,yworld_base)
    turtle.title("Welcome to Turtle Racing!")
    turtle.setup(xwin,ywin,0,0)
    turtle.setworldcoordinates(-xworld/2,0,xworld/2,yworld)
    turtle.penup()
    turtle.goto(0,y_title)
    turtle.write("Turtle Racing",move=False,align="center",font=("Arial",int(32*ts),"normal"))
    turtle.tracer(n=0, delay=None)
    turtle_tracks(ntot,y,tw,st,lt)
    start_line(s,y,ls)
    finishflag(fin,y,lf,b,sq)
    turtle.tracer(n=1, delay=None)
    sp=s-tw*0.68
    goal_zone=sp+l+2.05*tw
    if turtle_name==[]:
        turtle_name=turtle.textinput("Turtle Information","What is the name of your turtle?")
        racer_color=turtle.textinput("Turtle Information","What color is your turtle?")
    racer=turtle.Turtle(shape="turtle",visible=False)
    racer.fillcolor(racer_color) 
    racer.speed(0)
    racer.turtlesize(ts,ts,0)
    racer.penup()
    racer.goto(sp,yr)
    racer.speed(1)
    racer.st()
    clicker=turtle.Turtle(visible=False)
    clicker.penup()
    clicker.resizemode("user")
    clicker.shapesize(ts*5,ts*5,ts*5)
    clicker.speed(3)
    turtle.delay(6)
    clicker.goto(ax,ay)
    clicker.fillcolor("red")
    fake_clicker=clicker.clone()
    fake_clicker.ht()
    a={}
    key=[0]*n
    turtle.delay(1)
    for i in range(n):
        yr=yr-tw
        key[i]=f"turtle{i}"
        a[key[i]]=turtle.Turtle(shape="turtle",visible=False)
        a[key[i]].ht()
        a[key[i]].speed(0)
        a[key[i]].shapesize(1,1,0)
        a[key[i]].turtlesize(ts,ts,0)
        a[key[i]].fillcolor(random.sample(range(0,255),3))
        a[key[i]].penup()
        a[key[i]].goto(sp,yr)
        a[key[i]].speed(1)
        a[key[i]].st()
    size_instructions=int(10*ts)
    instructor=turtle.Turtle(visible=False)
    instructor.penup()
    instructor.speed(3)
    instructor.goto(0,y+0.1*tw)
    turtle.delay(0)
    instructor.write("Click fast and "+turtle_name+" will run fast!",move=False,align="center",font=("Arial",size_instructions,"normal"))
    start_race(ax,ay,ts)
    turn=0
    k=list(range(n))
    z=len(k)
    clicker.st()
    run_forrest_run(racer,clicker)
    while z>0:
        t=random.choice(k)
        #key=f"turtle{t}"
        a[key[t]].fd(1)
        if turn==difficulty and racer.xcor()!=(goal_zone):
            turtle.delay(1)
            turn=0
        else:
            turtle.delay(0)
            turn=turn+1
        if a[key[t]].xcor()>=(sp+l):
            turtle.delay(1)
            a[key[t]].speed(1)
            if clicker.isvisible():
                fake_clicker.st()
                clicker.ht()
            a[key[t]].goto(goal_zone,a[key[t]].ycor())
            if fake_clicker.isvisible():
                clicker.st()
                fake_clicker.ht()
            k.remove(t)
            z=len(k)
        if racer.xcor()>=(sp+l) and racer.xcor()!=(goal_zone) or z==0 and racer.xcor()!=(goal_zone):
            clicker.ht()
            instructor.clear()
            turtle.delay(1)
            racer.speed(1)
            racer.goto(goal_zone,racer.ycor())
            turtle.delay(0)
            ranking=ntot-z
    turtle.delay(0)
    ranker=turtle.Turtle(visible=False)
    ranker.penup()
    ranker.goto(0,y+2*tw)
    size_title=int(20*ts)
    size_subtitle=int(16*ts)
    size_button_description=int(12*ts)
    if ranking==1:
        difficulty=difficulty+1
        ranker.color("green")
        ranker.write(str(ranking)+". Place!",move=False, align="center",font=("Arial",(size_title),"normal"))
        turtle.delay(100)
        ranker.goto(0,y+0.8*tw)
        ranker.write("Congratulations, "+turtle_name+" is the fastest turtle!",move=False, align="center",font=("Arial",size_subtitle,"normal"))
    if ranking>1 and ranking<(ntot+1)/2:
        ranker.color("dark green")
        ranker.write(str(ranking)+". Place!",move=False, align="center",font=("Arial",size_title,"normal"))
        turtle.delay(100)
        ranker.goto(0,y+0.8*tw)
        ranker.write("Not bad! "+turtle_name+" is pretty fast!",move=False, align="center",font=("Arial",size_subtitle,"normal"))
    if ranking==(ntot+1)/2:
        ranker.color("black")
        ranker.write(str(ranking)+". Place!",move=False, align="center",font=("Arial",size_title,"normal"))
        turtle.delay(100)
        ranker.goto(0,y+0.8*tw)
        ranker.write(turtle_name+" could be faster... "+turtle_name+" could also be slower!",move=False, align="center",font=("Arial",size_subtitle,"normal"))
    if ranking<ntot and ranking>(ntot+1)/2:
        ranker.color("dark red")
        ranker.write(str(ranking)+". Place!",move=False, align="center",font=("Arial",size_title,"normal"))
        turtle.delay(100)
        ranker.goto(0,y+0.8*tw)
        ranker.write("Hmmm... "+turtle_name+" is pretty slow!",move=False, align="center",font=("Arial",size_subtitle,"normal"))
    if ranking==ntot:
        if difficulty>0:
            difficulty=difficulty-1
        ranker.color("red")
        ranker.write(str(ranking)+". Place!",move=False, align="center",font=("Arial",size_title,"normal"))
        turtle.delay(100)
        ranker.goto(0,y+0.8*tw)
        ranker.write("Oh no! No turtle is slower than "+turtle_name+"!",move=False, align="center",font=("Arial",size_subtitle,"normal"))
    turtle.delay(100)
    ranker.home()
    turtle.delay(0)
    ranker.clear()
    turtle.goto(0,y+2.2*tw)
    turtle.write("Does "+turtle_name+" want to race again?",move=False, align="center",font=("Arial",size_subtitle,"normal"))
    turtle.delay(0)
    yes=turtle.Turtle(shape="circle",visible=False)
    no=turtle.Turtle(shape="circle",visible=False)
    yes.speed(0)
    no.speed(0)
    yes.fillcolor("dark green")
    no.fillcolor("dark red")
    yes.shapesize(ts,ts,2*ts)
    no.shapesize(ts,ts,2*ts)
    yes.penup()
    no.penup()
    turtle.delay(400)
    yes.goto(-4*tw,y+0.2*tw)
    no.goto(4*tw,y+0.2*tw)
    turtle.delay(0)
    yes.write("Yes, "+turtle_name+" is ready!",move=False,align="center",font=("Arial",size_button_description,"normal"))
    yes.goto(-4*tw,y+1.5*tw)
    yes.st()
    turtle.delay(0)
    no.write("No, "+turtle_name+" is tired!",move=False,align="center",font=("Arial",size_button_description,"normal"))
    no.goto(4*tw,y+1.5*tw)
    turtle.delay(150)
    no.st()
    def yes_active(x,y):
        yes.pendown()
        turtle.delay(0)
        yes.fillcolor("light green")
        no.fillcolor("dark red")
    def no_active(x,y):
        no.pendown()
        turtle.delay(0)
        no.fillcolor("red")
        yes.fillcolor("dark green")
    def again(x,y):
        turtle.delay(0)
        yes.fillcolor("light green")
        no.fillcolor("dark red")
        no.clear()
        no.ht() 
    def no_more(x,y):
        turtle.delay(0)
        no.fillcolor("red")
        yes.fillcolor("green")
        yes.clear()
        yes.ht()
    yes.onclick(yes_active)
    yes.onrelease(again)
    no.onclick(no_active)
    no.onrelease(no_more)
    while yes.isvisible()==True and no.isvisible()==True:
        if no.isdown()==False:
            turtle.delay(400) 
            no.fillcolor("dark red")
        turtle.delay(0)   
        no.fillcolor("red")
        if yes.isdown()==False:
            turtle.delay(400)
            yes.fillcolor("dark green")
        turtle.delay(0)
        yes.fillcolor("light green")
    if yes.isvisible()==True:
        play=1
    if no.isvisible()==True:
        play=0
    return turtle_name,racer_color,play,difficulty
turtle_name=[]
racer_color=[]
n=6
l=500
difficulty=0
play=1
while play==1:
        turtle_name,racer_color,play,difficulty=race(turtle_name,racer_color,n,l,difficulty)
        turtle.clearscreen()
if play==0:
    turtle.bye()
import turtle
def yes(yes_size,yes_x,yes_y):
    yes=turtle.Turtle(shape="circle",visible=False)
    yes.speed(0)
    yes.fillcolor("dark green")
    yes.shapesize(yes_size,yes_size,2*yes_size)
    yes.penup()
    yes.goto(yes_x,yes_y)
    yes.write("Yes!",move=False,align="center",font=("Arial",30,"normal"))
    yes.goto(yes_x,yes_y+30)
    yes.st()
    def again(x,y):
        play_again=1
        return play_again
    play_again=yes.onclick(again)
    
    return play_again
play_again=yes(10,0,50)
print(play_again)
turtle.mainloop()
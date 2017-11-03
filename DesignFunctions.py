def jump (t,x,y):
    t.home()
    t.penup()
    t.goto(x,y)
    t.pendown()

def spiral (t,dist,angle):
    t.forward(dist)
    t.right(angle)
    
def star (t,dist,angle):
    t.forward(dist)
    t.right(angle)

def spd (b,t,r,d,l,speed):
    b.speed(speed)
    t.speed(speed)
    r.speed(speed)
    d.speed(speed)
    l.speed(speed)

def hide (b,t,r,d,l):
    b.hideturtle()
    t.hideturtle()
    r.hideturtle()
    d.hideturtle()
    l.hideturtle()
    

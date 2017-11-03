import turtle
from random import *
from DesignFunctions import *
turtle.colormode(255) #use for RGB colors
bob = turtle.Turtle()
tod = turtle.Turtle()
ren = turtle.Turtle()
dan = turtle.Turtle()
link = turtle.Turtle()
spd(bob,tod,ren,dan,link,0) #speed of all the turtles
wn=turtle.Screen()
wn.bgcolor(0,0,0)#changes background color to black
bob.color(255,255,255)
r = randint(0,255)#allows for random colors
g = randint(0,255)
b = randint(0,255)
hide(bob,tod,ren,dan,link)#hides turtle

for times in range (400): #draws a flower kind of thing
    bob.pencolor(r,255,255)
    star(bob,times,133)
jump(tod,-500,-200)
for times in range (110):#draws a pentagon spiral
    tod.pencolor(r,g,b)
    spiral(tod,times,85.911)
jump(ren,500,-200)
for times in range (100):
    ren.pencolor(r,g,b)
    spiral(ren,times,75.911) #draws a square spiral
jump(dan,-500,200)
for times in range (100):
    dan.pencolor(r,g,b)
    spiral(dan,times,75.911)
jump(link,500,200)
for times in range (110):
    link.pencolor(r,g,b)
    spiral(link,times,85.911)

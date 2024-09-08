from turtle import *

#we want to paint house

#step 1:  draw a square
shape("turtle")
speed(10)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()
begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

print("day 1 homework")

#drawing left window


color("blue")
left(120)
forward(40) 
right(90)
forward(40)
right(90)
forward(40)
end_fill()

#drawing right window


right(90)
color("purple")
forward(40)
right(90)
forward(160)
color("blue")
right(90)
forward(40)
left(90)
forward(40)
end_fill()

color("purple")
left(90)
forward(40)
left(90)
forward(40)









exitonclick()
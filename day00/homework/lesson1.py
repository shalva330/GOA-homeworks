from turtle import*


#we want to paint a house

#step 1: draw a square
speed(7)
width(7)
color("purple")
forward (200)
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
color("yellow")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of drawing

#drawing the window
color("brown")
right(150)
pendown()
right(180)
forward(70)
left(90)
forward(200)
left(90)
forward(75)
left(90)
forward(200)
left(90)
forward(45)
right(0)
forward(30)
right(270)
forward(100)
left(90)
forward(75)
left(90)
forward(100)
forward(5)
right(270)
forward(40)
right(270)
forward(200)




exitonclick()




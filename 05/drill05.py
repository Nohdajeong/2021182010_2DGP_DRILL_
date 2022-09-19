import turtle

def move_turtle_up():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def move_turtle_down():
    turtle.stamp()
    turtle.setheading(-90)
    turtle.forward(50)

def move_turtle_right():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def move_turtle_left():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def restart():
    turtle.reset()

turtle.shape("turtle")

turtle.onkey(move_turtle_up, 'w')
turtle.onkey(move_turtle_down, 's')
turtle.onkey(move_turtle_right, 'd')
turtle.onkey(move_turtle_left, 'a')

turtle.onkey(restart, 'Escape')
turtle.listen()

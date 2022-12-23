from turtle import Turtle, Screen
tim = Turtle()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turning_left():
    tim.left(10)

def turning_right():
    tim.right(10)

def clearing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

s = Screen()
s.listen()
s.onkeypress(key="w", fun=move_forward)
s.onkeypress(key="s", fun=move_backward)
s.onkeypress(key="a", fun=turning_left)
s.onkeypress(key="d", fun=turning_right)
s.onkeypress(key="c", fun=clearing)
s.exitonclick()
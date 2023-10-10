import turtle
import random
import time

# Create a game board screen object
gameBoard = turtle.Screen()
gameBoard.title("Catch Turtle v1.0")
gameBoard.bgcolor("white")

# Write main head
turtle_head = turtle.Turtle()
turtle_head.color("purple")
turtle_head.hideturtle()
turtle_head.speed(0)
turtle_head.penup()
turtle_head.setposition(x=0, y=350)
turtle_head.pendown()
turtle_head.write("#If you're fast, Catch the Turtle...", move=False, font=("Verdana", 15, "normal"), align="center")

# Write Time head
turtle_time = turtle.Turtle()
turtle_time.color("green")
turtle_time.hideturtle()
turtle_time.speed(0)
turtle_time.penup()
turtle_time.setposition(x=0, y=300)
turtle_time.pendown()
turtle_time.write("Time: ", move=False, font=("Verdana", 18, "normal"), align="center")

# Create dynamic timer
turtle_dy_timer = turtle.Turtle()
turtle_dy_timer.color("green")
turtle_dy_timer.hideturtle()
turtle_dy_timer.speed(0)
turtle_dy_timer.penup()
turtle_dy_timer.setposition(x=65, y=300)

# Write Score head
turtle_score = turtle.Turtle()
turtle_score.color("blue")
turtle_score.hideturtle()
turtle_score.speed(0)
turtle_score.penup()
turtle_score.setposition(x=0, y=275)
turtle_score.pendown()
turtle_score.write("Score: ", move=False, font=("Verdana", 18, "normal"), align="center")

# Create dynamic timer
turtle_dy_score = turtle.Turtle()
turtle_dy_score.color("blue")
turtle_dy_score.hideturtle()
turtle_dy_score.speed(0)
turtle_dy_score.penup()
turtle_dy_score.setposition(x=65, y=275)


# Draw a frame
turtle_frame = turtle.Turtle()
turtle_frame.color("black")
turtle_frame.hideturtle()
turtle_frame.speed(0)
turtle_frame.penup()
turtle_frame.setposition(x=-250, y=250)
turtle_frame.pendown()

for i in range(4):
    turtle_frame.forward(500)
    turtle_frame.left(-90)


turtle_runner = turtle.Turtle()
turtle_runner.shape("turtle")
turtle_runner.shapesize(1.5)
turtle_runner.color("green")
turtle_runner.penup()
turtle_runner.setposition(x=0, y=0)


def clickedTurtle(x1, y1):
    global score_turtle
    score_turtle += 1
    turtle_dy_score.clear()
    turtle_dy_score.write(f"{score_turtle}", move=False, font=("Verdana", 18, "normal"), align="right")


score_timer = 21
score_turtle = 0
while True:
    if score_timer == 0:
        turtle_dy_timer.clear()
        turtle_time.clear()
        turtle_time.color("red")
        turtle_time.write("Game Over!", move=False, font=("Verdana", 18, "normal"), align="center")
        break
    else:
        turtle_runner.onclick(clickedTurtle)
        score_timer -= 1
        turtle_dy_timer.clear()
        turtle_dy_timer.write(f"{score_timer}", move=False, font=("Verdana", 18, "normal"), align="right")
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        turtle_runner.goto(x, y)
        time.sleep(.5)

turtle.mainloop()

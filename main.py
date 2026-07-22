from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

ball = Ball()
score = Scoreboard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")

paddle_right = Paddle(370)
paddle_left = Paddle(-370)

screen.listen()

screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

game_is_going = True
timming = 0.1
while game_is_going:
	time.sleep(timming)
	screen.update()
	ball.move()
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()
	
	if ball.distance(paddle_right) < 50 and ball.xcor() > 340 or ball.distance(paddle_left) < 50 and ball.xcor() < -340:
		ball.bounce_x()
		timming = max(0.01, timming - 0.02)
	
	if ball.xcor() > 380:
		timming = 0.1
		ball.reset()
		score.l_point()
	
	if ball.xcor() < -380:
		timming = 0.1
		ball.reset()
		score.r_point()

screen.exitonclick()

import turtle
import os


wn = turtle.Screen()
wn.title("The Pong Game Window")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0

os.system("open /Users/mac/Music/酷狗音乐/BQ/Rose.mp3")          # play music when the game started ( run on mac )

class Paddle:
    def __init__(self, coordinate_x):
        self.coordinate_x = coordinate_x
        self.coordinate_y = 0
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x=coordinate_x, y=0)

    def paddle_move_up(self):
        paddle = self.paddle
        self.coordinate_y = self.paddle.ycor()
        self.coordinate_y += 20
        return paddle.sety(self.coordinate_y)

    def paddle_move_down(self):
        paddle = self.paddle
        self.coordinate_y = self.paddle.ycor()
        self.coordinate_y -= 20
        paddle.sety(self.coordinate_y)


class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.dx = 2
        self.dy = 2
        self.ball.speed(0)
        self.ball.shape("square")          # Create a ball if size 20 * 20 pixels
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)

    def move(self):
        self.ball.setx(self.ball.xcor()+self.dx)
        self.ball.sety(self.ball.ycor()+self.dy)

    def check(self):
        if self.ball.xcor() > 390:
            self.ball.setx(390)
            self.dx *= -1
        if self.ball.xcor() < -390:
            self.ball.setx(-390)
            self.dx *= -1
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.dy *= -1
        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.dy *= -1


paddle_a = Paddle(-350)
paddle_b = Paddle(350)

wn.listen()
wn.onkeypress(paddle_a.paddle_move_up, 'w')
wn.onkeypress(paddle_a.paddle_move_down, 's')
wn.onkeypress(paddle_b.paddle_move_up, 'Up')
wn.onkeypress(paddle_b.paddle_move_down, 'Down')

ball = Ball()

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.up()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0 ", align="center", font=("Courier", 24, "normal"))

while True:
    wn.update()

    ball.move()
    ball.check()

    if ball.ball.xcor() < -340 and (-40 + paddle_a.paddle.ycor() < ball.ball.ycor() < 40 + paddle_a.paddle.ycor()):
        ball.ball.setx(-340)
        ball.dx *= -1
        score_a = score_a + 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b} ", align="center", font=("Courier", 24, "normal"))

    if ball.ball.xcor() > 340 and (-40 + paddle_b.paddle.ycor() < ball.ball.ycor() < 40 + paddle_b.paddle.ycor()):
        ball.ball.setx(340)
        ball.dx *= -1
        score_b = score_b + 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b} ", align="center", font=("Courier", 24, "normal"))





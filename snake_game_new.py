# create the snake body
# move the snake
# control the snake
# detect collision with the food
# create a scoreboard
# detect collision with wall
# detect collision with tail

from turtle import Screen
# from random import randint
import time
from snake_class_new import Snake
from food_new import Food
from scoreboard_new import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Abhi's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

def pause_game():
    screen.numinput("Game Paused","Game Paused")

screen.listen()
# screen.onkey(fun= pause_game,key='space')

screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')
# screen.onkey(fun= snake.play,key='Return')

# file = open("high_score_file.txt")
# cont = file.read()
# path = "C:\Users\apalatkar\Documents\PYTHON_CPP\PYTHON\Udemy"
with open("/Users/apalatkar/Documents/PYTHON_CPP/PYTHON/Udemy/sample_doc.txt","w") as file:
    file.write("Hello")


with open('../../Udemy/sample_doc.txt',mode='r') as file1:
    file1.read()


Game_ON = 1
while Game_ON:
    screen.update()
    time.sleep(0.05)
    snake.move()
    if snake.head.distance(food) < 15:
        # food.reset()
        food.refresh()
        snake.extend()
        score.keep_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset_game()
        snake.snake_reset()

    for dot in snake.dot:
        if dot == snake.head:
            pass
        elif snake.head.distance(dot) < 5:
            score.reset_game()

screen.exitonclick()

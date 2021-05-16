from turtle import Turtle
<<<<<<< HEAD
from random import randint
=======
import random
>>>>>>> bf14fe4e2baf23a780953c07aa79f66a7ba33bfb


class Food(Turtle):

    def __init__(self):
        super().__init__()
<<<<<<< HEAD
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('cyan')
        self.speed('fastest')
        self.goto(randint(-280, 280), randint(-280, 280))

    def refresh(self):
        return self.__init__()
=======
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
>>>>>>> bf14fe4e2baf23a780953c07aa79f66a7ba33bfb

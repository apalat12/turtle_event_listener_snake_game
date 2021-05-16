from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DIST = 10


class Snake:

    def __init__(self):
        self.dot = []
        self.create_snake()
        self.head = self.dot[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        t1 = Turtle()
        t1.shape('square')
        t1.color('white')
        t1.shapesize(0.5, 0.5)
        t1.penup()
        t1.goto(position)
        # t1.speed('fastest')
        self.dot.append(t1)

    def extend(self):
        self.add_segment(self.dot[-1].pos())

    def move(self):
        for i in range(len(self.dot) - 1, 0, -1):
            new_x = self.dot[i - 1].xcor()
            new_y = self.dot[i - 1].ycor()
            self.dot[i].goto(new_x, new_y)
        self.dot[0].fd(MOVE_DIST)

    def up(self):
        if self.head.heading() != 270:
            return self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            return self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            return self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            return self.head.setheading(0)

    def snake_reset(self):
        for seg in self.dot:
            seg.goto(1000,-1000)
        self.__init__()



from turtle import Turtle

with open("high_score_file.txt", mode='r') as file:
    cont = file.read()
    # print(cont)

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.high_score = int(cont)
        self.penup()
        self.goto(0, 270)
        self.write("Score: {} High Score:{}".format(self.score,self.high_score), move=False, align="center", font=("Arial", 16, "bold"))
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write("Score: {} High Score:{}".format(self.score,self.high_score), move=False, align="center", font=("Arial", 16, "bold"))

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("high_score_file.txt",mode='w')
            file.write(str(self.high_score))
            file.close()
        self.score = 0
        self.update_scoreboard()

    def keep_score(self):
        self.score += 1
        self.update_scoreboard()


    # def game_over(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align="center", font=("Arial", 16, "bold"))



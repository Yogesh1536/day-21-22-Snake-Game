from turtle import Turtle

FONT = ('Courier', 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.setpos(0, 270)
        self.write(f'score : {self.score}', align='center', font=FONT)
        self.hideturtle()

    def game_over(self):
        self.setpos(0, 0)
        self.write('Game Over', align='center', font=FONT)


    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f'score : {self.score}', align='center', font=FONT)

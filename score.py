from turtle import Screen

FONT = ("Courier", 24, "normal")


class Score():

    def __init__(self):
        self.n = 0
        self.txt = Screen()
        

    def ask_for_state(self):
        self.answer = self.txt.textinput(title=f"{self.n}/50 States Correct", prompt="What's another state name?")
        

    # update the score
    def update_score(self):
        self.n += 1





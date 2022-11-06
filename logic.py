import pandas
from turtle import Turtle




class Game(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.data = pandas.read_csv("50_states.csv")     
        self.states = {}
        self.states_to_dict()

    
    # states are done in a dict format
    def states_to_dict(self):
        i = 0
        for state in self.data["state"]:
            state_coor = self.data[["x", "y"]].apply(tuple, axis=1)[i]
            self.states[state] = state_coor
            i += 1
    
    
    # check whether the state exists
    def exists(self, state):
        if state in self.states:
            self.goto(self.states[state])
            self.write(state)
            return True
        
        return False

    def missed(self, state):
        if state in self.states:
            self.states.pop(state)

    def final_missed_states(self):
        df = pandas.DataFrame(self.states.keys())
        df.to_csv("Missed-States.csv", index=False)

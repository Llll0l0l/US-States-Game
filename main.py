import turtle
from turtle import Screen
from score import Score
from logic import Game


# screen properties
screen = Screen()
screen.setup(725, 491)
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
screen.update()


score = Score()
game = Game()

game_is_on = True



# while game is on ...
while game_is_on:


    score.ask_for_state()

    # update score
    if game.exists(score.answer.title()):
        game.missed(score.answer.title())
        score.update_score()


    # end the game
    if score.n == 50 or score.answer.lower() == "exit":
        game.final_missed_states()
        game_is_on = False

screen.exitonclick()

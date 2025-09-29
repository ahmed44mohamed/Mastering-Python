
# Importing
import turtle
import pandas

# Setup
screen = turtle.Screen ()
screen.title ("U.S. states Game")
image = "./csv_files_pandas_lib/projects/us_states_game/blank_states_img.gif"
screen.addshape (image)
screen.setup (725, 491)
turtle.shape (image)
FONT = ("Arial", 7, "bold")
writer = turtle.Turtle ()

# Main data
correct_answer = 0

# Main
all_data = pandas.read_csv ("./csv_files_pandas_lib/projects/us_states_game/50_states.csv")
states_data = all_data.state.to_list ()
correct_guesses = []
while correct_answer < 50:
    answer_state = screen.textinput (title= f"{correct_answer} / 50", prompt= "What's another state's name?").title ()

    # If user want to exit from the game
    if answer_state == "Exit":
        states_not_guessed = list (set (states_data) - set (correct_guesses))
        missing_states = [state for state in states_data if state in states_not_guessed]
        new_csv_states_not_guessed = pandas.DataFrame (missing_states)
        new_csv_states_not_guessed.to_csv ("./csv_files_pandas_lib/projects/us_states_game/not_guessed.csv")
        break

    # If user's guess right
    if answer_state in states_data:
        correct_answer += 1
        correct_guesses.append (answer_state)
        x = float (all_data [all_data.state == answer_state].x)
        y = float (all_data [all_data.state == answer_state].y)
        writer.penup ()
        writer.hideturtle ()
        writer.goto (x, y)
        writer.write (answer_state, font= FONT)

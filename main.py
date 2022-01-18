from turtle import Screen, Turtle
import pandas
import time

turtle = Turtle()
text_writer = Turtle()
wrong_answer_writer = Turtle()
already_answered_writer = Turtle()
warning_writer = Turtle()

text_writer.hideturtle()
wrong_answer_writer.hideturtle()
already_answered_writer.hideturtle()
warning_writer.hideturtle()

text_writer.penup()
wrong_answer_writer.penup()
already_answered_writer.penup()
warning_writer.penup()
turtle.penup()

guessed_states = 0

states_already_guessed = []

screen = Screen()
screen.title(f"{guessed_states}/50 States Correct")
screen.setup(width=725, height=491)
screen.tracer(0)

# Read States data :
states_data = pandas.read_csv("50_states.csv")
# print(states_data.state)

# add shape image file (turtle only work with .gif)
image = "blank_states_img.gif"
screen.addshape(image)

# set screen shape from image file
turtle.shape(image)

# Turn the states' series data into a python list.
list_of_states = states_data.state.to_list()

while len(states_already_guessed) < 51:
    # Ask the user the answer
    screen.update()
    time.sleep(0.1)
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # Create a dictionary of states_to_learn
        states_to_learn = {"States To Learn ": list_of_states}
        # Turn the dictionary into a DataFrame
        states_to_learn_data_frame = pandas.DataFrame(states_to_learn)
        # Turn the DataFrame into a csv file
        states_to_learn_data_frame.to_csv("states_to_learn.csv")
        break

    if answer_state in states_already_guessed:
        already_answered_writer.write("You've already answered this!")

    elif answer_state in list_of_states:
        state_data = states_data[states_data.state == answer_state]
        x_cor = int(state_data["x"])
        y_cor = int(state_data["y"])
        text_writer.goto(x_cor, y_cor)
        text_writer.write(answer_state)
        guessed_states = guessed_states + 1
        screen.title(f"{guessed_states}/50 States Correct")
        states_already_guessed.append(answer_state)

        wrong_answer_writer.clear()
        already_answered_writer.clear()

    elif answer_state not in list_of_states:
        print("Wrong! Guess again")
        wrong_answer_writer.write("Wrong! Guess Again")

# states_to_learn.csv

# Remove guessed states from list of states
for item in states_already_guessed:
    list_of_states.remove(item)

screen.mainloop()

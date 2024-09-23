import turtle
import pandas
screen=turtle.Screen()
screen.title("US States Game")
image="blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
all_states=data.state.tolist()



guess_states=[]
missing_states=[]
while len(guess_states)<50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="What's another states name?").title()
    if answer_state=="Exit":
        for state in all_states:
            if state not in guess_states:
                missing_states.append(state)
            new_data=pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")



        break

    if answer_state in all_states:
        guess_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)




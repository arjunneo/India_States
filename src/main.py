import turtle
import pandas

t = turtle.Turtle()
scrn = turtle.Screen()
scrn.setup(width=650, height=650)
India_Image = "Images/India_Map_States_and_UTs_425_500.gif"
# India_Image = "/Neo/Learning/Python/MyOwn/India_States/Images/India_Map_States_and_UTs_425_500.gif"
# India_Image = "C:\\Neo\\Learning\\Python\\MyOwn\\India_States\\Images\\India_Map_States_and_UTs.gif"
# India_Image = "/src/India_Map_States_and_UTs.gif"
t.hideturtle()
t.penup()
scrn.title("India States and Union Territories")
scrn.addshape(India_Image)
turtle.shape(India_Image)

# Get x and y coordinates of mouse click -- this code is to identify the coordinates
# def get_mouse_click_coor(x,y):
#    print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# Load data file

# data_frame = pandas.read_csv("/Neo/Learning/Python/MyOwn/India_States/src/India_States_and_UTs.csv")
data_frame = pandas.read_csv("src/India_States_and_UTs.csv")
# print(data)

all_states_UTs = data_frame.region.to_list() # data_frame[data_frame["region_type"] == "State"] -- both statements are same
# print(all_states_UTs)
all_states = data_frame.region[data_frame["region_type"] == "State"]
# print(all_states)
all_UTs = data_frame.region[data_frame["region_type"] == "Union Territory"]
# print(all_UTs)

# data_row = data_frame.head(20)
# print(data_row)

# data_index = data_frame.index
# print(data_index)

# print(data_frame["region_type"])
# print(data_frame.loc[:, ["region", "x", "y"]])

guessed_states = []

for region in range(0, len(data_frame)):
    state_name = scrn.textinput(f"{len(guessed_states)}/36 States and UTs correct", "Enter a State or UT Name ").title()

    if (state_name == "Exit"):
        break
    
    # data_row = data_frame.loc[region, ["region", "x", "y"]] -- this is to get each row using for loop
    data_row = data_frame[data_frame["region"] == state_name]
    if not data_row.empty:
        x_cord = int(data_row["x"].item())
        y_cord = int(data_row["y"].item())

        t.goto(x_cord, y_cord)
        t.write(state_name, font=("Verdana", 8, "bold"))
        
        guessed_states.append(state_name)




scrn.mainloop()

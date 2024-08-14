import turtle
import time

t = turtle.Turtle()
# Basic outline
print("Hello! This is a program that will create a y = ax equation for whatever points you would like to add.")    
time.sleep(1)


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# Basic graph outline
t.speed('fastest')
t.forward(250)
t.backward(500)
t.forward(250)
t.left(90)
t.forward(250)
t.backward(500)
t.forward(250)
t.right(90)
t.penup()
t.goto(80, -30)
t.pendown()
font = ("Times New Roman", 15, "normal")
t.write("X-Axis", font=font, align="left")

# Write "Y-Axis" label vertically, rotated 90 degrees
t.penup()
t.goto(-40, 100)
t.left(90)  # Rotate turtle to face upwards
t.pendown()
t.write("Y-Axis", font=font, align="center")
t.right(90)
t.penup()
t.goto(0, 0)
t.pendown()


def coordPlot(xcoordinate, ycoordinate, scale):
    t.penup()
    t.goto(xcoordinate * scale, ycoordinate * scale)
    t.pendown()
    t.dot(10, 'blue')
    t.penup()
    t.goto(0, 0)
    t.pendown()
    

#actual program
number_point = int(1)

turn_over = False

points = []

xSum = 0
ySum = 0

Max_value = 0


while turn_over == False:
    if number_point == 1:
        xCoord = input("Please input an x-coordinate for your 1st point. ")
    if number_point == 2:
        xCoord = input('Please input an x-coordinate for your 2nd point. ')
    if number_point == 3:
        xCoord = input('Please input an x-coordinate for your 3rd point. ')
    elif number_point >= 4:
        xCoord = input(f'Please input an x-coordinate for your {number_point}th point. ')


    while is_float(xCoord) == False:        
        xCoord = input("Please input an integer or decimal for your x-coordinate. ")

    xCoord = float(xCoord)

    if abs(xCoord) > Max_value:
        Max_value = abs(xCoord)

    xSum += xCoord
    
    if number_point == 1:
        yCoord = input("Please input a y-coordinate for your 1st point. ")
    if number_point == 2:
        yCoord = input('Please input a y-coordinate for your 2nd point. ')
    if number_point == 3:
        yCoord = input('Please input a y-coordinate for your 3rd point. ')
    elif number_point >= 4:
        yCoord = input(f'Please input a y-coordinate for your {number_point}th point. ')

    while is_float(yCoord) == False:
        yCoord = float(input("Please input an integer or decimal for your y-coordinate. "))

    yCoord = float(yCoord)

    if abs(yCoord) > Max_value:
        Max_value = abs(yCoord)

    ySum += yCoord
    
    points.append((xCoord, yCoord))
    
    number_point += 1
    
    graph_end = input("Would you like to put in another point or would you like for me to do a y = a * x prediction? Type 'y' if you would like for me to add another point and anything else if not. ")

    if graph_end != 'y':
        turn_over = True

scale = (200 / Max_value)

for x, y in points:
    coordPlot(x, y, scale)
    time.sleep(1)
    

xSumRound = round(xSum, 5)



ySumRound = round(ySum, 5)



print('\n')
print(f'The equation that best fits your points is approximately y = {ySumRound / xSumRound} * x. ')
    

 
    
    















           

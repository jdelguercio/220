"""
Name: <Joey Del Guercio>
<ProgramName>.py

Problem: <All of these functions solve simple math problems by prompting the user for a 1-3 inputs>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    shooters_percentage = shots_made / total_shots
    print("Shooting Percentage: ", shooters_percentage * 100, "%")

def coffee():
    lbs_coffee = eval(input("How many pounds of coffee would you like? "))
    coffee_cost = lbs_coffee * 10.5
    shipping_cost = lbs_coffee * .86
    fixed_cost = 1.5
    total = coffee_cost + shipping_cost + fixed_cost
    print("Your total is: ", total)



def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel? "))
    miles = kilometers / 1.61
    print("That's", miles, "miles!")


if __name__ == '__main__':
    pass
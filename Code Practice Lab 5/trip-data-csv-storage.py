import pandas
import os

def validate_input(prompt, value_type):
    while True:    
        user_input = input(prompt)
        try:
            user_input = float(user_input)
            if user_input < 0:
                print(f"{value_type} cannot be negative. Please enter a valid number.")
                continue
            return user_input
        except ValueError:
            print("Invalid input. Please enter a numeric value for miles driven.")

def validate_y_or_n(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in ['y', 'n']:
            return user_input
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

print("The Miles Per Gallon Program")

while True:

    if os.path.exists("trip-data.csv"):
        if pandas.read_csv("trip-data.csv").empty:  
            print("The CSV file is empty. Creating a new one.")
        else:
            print()
            print(pandas.read_csv("trip-data.csv"))
    else:
        print("The CSV file does not exist. Creating a new one.")

    print()

    miles_driven = validate_input("Enter miles driven: ", "Miles driven")

    gallons_of_gas = validate_input("Enter gallons of gas used: ", "Gallons of gas")

    miles_per_gallon = round(miles_driven / gallons_of_gas, 2)
    print(f"Miles Per Gallon: {miles_per_gallon}")

    data = {
        "Distance": [miles_driven],
        "Gallons": [gallons_of_gas],
        "MPG": [miles_per_gallon]
    }

    df = pandas.DataFrame(data)

    df.to_csv("trip-data.csv", mode='a', header=not os.path.exists("trip-data.csv"), index=False)

    print()

    print(pandas.read_csv("trip-data.csv"))

    print()

    more_entries = validate_y_or_n("More entries? (y or n): ")
    if more_entries.lower() != "y":
        break
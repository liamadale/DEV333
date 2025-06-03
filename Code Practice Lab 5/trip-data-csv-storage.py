import pandas
import os

FILE_NAME = "trip-data.csv" # name of the CSV file to store trip data

def validate_input(prompt, value_type): # validates user input for valid values for miles driven and gallons of gas used
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

def validate_y_or_n(prompt): # validates user input for yes or no
    while True:
        user_input = input(prompt).lower()
        if user_input in ['y', 'n']:
            return user_input
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def read_trips(): # reads the CSV file and loads it into memory
    all_trips_df = pandas.read_csv(FILE_NAME)
    return all_trips_df.values.tolist() # converts DataFrame to list of lists

def list_trips(all_trips): # displays the trip data in a readable format
    all_trips_df = pandas.DataFrame(all_trips, columns=["Miles Driven", "Gallons of Gas Used", "Miles Per Gallon"])
    print(all_trips_df.to_string(index=False)) # displays the DataFrame without the index

def write_trips(all_trips): # writes the trip data to the CSV file
    df = pandas.DataFrame(all_trips)
    df.to_csv(FILE_NAME, index=False)


print("The Miles Per Gallon Program")

all_trips = [] # initialize empty list to store trip data
more_entries = "y" # initialize variable to control loop
csv_not_empty = False # initialize variable to check if CSV file is empty

if os.path.exists(FILE_NAME): # if file exists
    df_check = pandas.read_csv(FILE_NAME) # read the CSV file
    if df_check.empty: # if file is empty
        print()
        print("The CSV file is empty. Creating a new one.")
    else: # if file is not empty
        print()
        print("The CSV file exists and is not empty. Loading data into memory.")
        all_trips = read_trips() # loads CSV into memory
        csv_not_empty = True
else: # file does not exist
    print()
    print("The CSV file does not exist. Creating a new one.")
    open(FILE_NAME, 'w')

while more_entries != "n": # continue until user enters "n"

    if csv_not_empty == True:
        print()
        list_trips(all_trips) # displays the CSV file

    print()

    miles_driven = validate_input("Enter miles driven: ", "Miles driven") # collects miles driven

    gallons_of_gas = validate_input("Enter gallons of gas used: ", "Gallons of gas") # collects gallons of gas used

    miles_per_gallon = round(miles_driven / gallons_of_gas, 2) # calculates miles per gallon
    print(f"Miles Per Gallon: {miles_per_gallon}") # displays miles per gallon

    current_trip = [miles_driven, gallons_of_gas, miles_per_gallon] # creates a list of the current trip data
    all_trips.append(current_trip) # appends the current trip data to the list of all trips


    print()

    list_trips(all_trips) # displays the CSV file

    print()

    write_trips(all_trips) # writes the trip data to the CSV file

    more_entries = validate_y_or_n("More entries? (y or n): ") # asks user if they want to enter more data

    csv_not_empty = True # sets variable to true to indicate that the CSV file is not empty
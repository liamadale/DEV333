def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

continue_program = True

# display a welcome message
print("The Miles Per Gallon program")
print()

while continue_program == True:
    # get input from the user

    miles_driven= get_positive_float("Enter miles driven: ")
    gallons_used = get_positive_float("Enter gallons of gas used: ")
    cost_per_gallon = get_positive_float("Enter cost per gallon: ")
    print()
    
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")

    # calculate and display miles per gallon.
    mpg = round((miles_driven / gallons_used),2)
    print("Miles Per Gallon:", mpg)
    print("Total Gas Cost:", round((gallons_used * cost_per_gallon),2))
    print("Cost Per Mile:", round((cost_per_gallon / mpg),2))
    print()

    while True:
        user_continue = input("Get entries for another trip (y/n)? ")
        print()
        if user_continue == "y":
            continue_program = True
            break
        elif user_continue == "n":
            continue_program = False
            break
        else:
            print("Please enter either 'y' or 'n'")
from helper import validate_and_execute

user_input = ""
while user_input != "x":
    user_input = input("Enter number of days and unit(H/M) separated by ':' (to exit type x)\n")
    if user_input == "x" or user_input == "X":
        break
    else:
        try:
            days_and_unit = user_input.split(":")
            days_and_unit_dictionary ={"days": days_and_unit[0], "unit": days_and_unit[1]}
            validate_and_execute(days_and_unit_dictionary)
        except:
            print("invalid input")
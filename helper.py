
def days_to_units(num_of_days, conv_unit):
    calculation_to_units = 0
    if conv_unit =="H" or conv_unit=="h":
        calculation_to_units=24
    elif conv_unit=="M"or conv_unit=="m":
        calculation_to_units=24*60
    else:
        return ("invalid time conversion")
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {conv_unit}"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        # we want to do conversion only for positive numbers
        if user_input_number>0:
            my_var = days_to_units(user_input_number,days_and_unit_dictionary["unit"])
            print(my_var)
        elif user_input_number==0:
            print("you entered a 0")
        else:
            print("you entered a negative number")
    except:
        print("invalid input")

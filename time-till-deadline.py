from datetime import datetime


user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
deadline_date = datetime.strptime(deadline,"%d.%m.%y")

#calc the days from now to deadline
current_date = datetime.today()
time_till = deadline_date-current_date

print(f"you have {time_till.days} days remaining to {goal}")
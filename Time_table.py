# Timetable program

# This program will be able to run the timetables for any number

user_num = int(input("Enter the number for which timetable you would like to be displayed : "))
multiplier_num = int()
for multiplier_num in range(1, 13):
    print(str(user_num) + " * " + str(multiplier_num) + " = " + str(user_num * multiplier_num))

import re
from datetime import time

def float_to_time(hours_float):
    hours, remainder = divmod(hours_float, 1)
    minutes = int(remainder * 60)
    return time(int(hours), minutes)

task_array = []
time_float_array =[]
time_array =[]

name = input("Enter Your Name: ")
task_number = int(input("Enter Your number of tasks you want to do: "))
count = 0

while count < task_number:
    count = count + 1
    print("===========================================")
    print("Please choose your tasks: ")
    print("===========================================")
    print("LG : Login")
    print("RG : Register")
    print("US : User")
    print("EMP : Employee")
    print("TS : Timesheets")
    task_input = input("Choose a 1 task: ")

    match task_input:
        case "LG":
            task = "Login"
        case "RG":
            task = "Register"
        case "US":
            task = "User"
        case "EMP":
            task = "Employee"
        case "TS":
            task = "Timesheets"
    task_array.append(task)
    work_hour = float(input("Enter your working hour for " + task  + " (in float, e.g 1.5 for 1 hour 30 minutes): "))
    time_float_array.append(work_hour)

    work_time = float_to_time(work_hour)
    time_array.append(work_time)

print(f"Summary of Tasks for {name}:")

for i in range(0,len(task_array)):
    print(task_array[i] + ", Working Hours: ", time_float_array[i], "(",time_array[i],")")
#    todo app, that app just write tasks to json.
#    Copyright (C) 2020  SUMER
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.



import json 
import time
import os.path
from colorama import init, Fore
filename = "Data.json"
from os import system
system("title "+"TODO")
init()
if os.path.exists(filename) == False:
    f = open(filename,"w+")
    f.write("{}")
    f.close()
while True:
    choice = input("[1] - write new task, [2] - check your tasks, [3] - delete task, [4] - Credits: ")
    if choice.isnumeric() == True:
        if int(choice) == 1:
            name = input("what name for task?: ")
            todo = input("what u need do?: ")
            Status = input("Status, [1] - Working on it, [2] - Stuck, [3] - Done, [4] - Waiting for review: ")
            DueDate = input("Due date: ")
            Priority = input("Priority, [1] - Urgent, [2] - High, [3] - Medium, [4] - Low: ")
            with open(filename, "r") as f:
                Tasks = json.load(f)
            ReadyStatus = ""
            PriorityStatus = ""
            if Status == "1":
                ReadyStatus = "Working on it"
            elif Status == "2":
                ReadyStatus = "Stuck"
            elif Status == "3":
                ReadyStatus = "Done"
            elif Status == "4":
                ReadyStatus = "Waiting for review"
            else:
                ReadyStatus = "Unknown"
            if Priority == "1":
                PriorityStatus = "Urgent"
            elif Priority == "2":
                PriorityStatus = "High"
            elif Priority == "3":
                PriorityStatus = "medium"
            elif  Priority == "4":
                PriorityStatus = "Low"
            else:
                PriorityStatus = "Unknown"
            Tasks[str(name)] = {
                'Name': name,
                'Todo': todo,
                'Status': ReadyStatus,
                'Time': DueDate,
                'Priority': PriorityStatus
            }
            with open(filename, "w",) as f:
                json.dump(Tasks, f, indent=4)
        elif int(choice) == 2:
            with open(filename, "r") as f:
                pseudotasklist = json.load(f)
            for TaskList in pseudotasklist.values():
                print("__________________________")
                print("Name: " + TaskList['Name'])
                print("Todo: " + TaskList['Todo'])
                if TaskList['Status'] == "Working on it":
                    print("Status:{} ".format(Fore.YELLOW) + TaskList['Status'])
                elif TaskList['Status'] == "Stuck":
                    print("Status:{} ".format(Fore.RED) + TaskList['Status'])
                elif TaskList['Status'] == "Done":
                    print("Status:{} ".format(Fore.GREEN) + TaskList['Status'])
                elif TaskList['Status'] == "Waiting for review":
                    print("Status:{} ".format(Fore.BLUE) + TaskList['Status'])
                else:
                    print("Status:{} ".format(Fore.MAGENTA) + TaskList['Status'])
                if TaskList['Priority'] == "Urgent":
                    print("{}Priority:{} ".format(Fore.WHITE, Fore.CYAN) + TaskList['Priority'])
                elif TaskList['Priority'] == "High":
                    print("{}Priority:{} ".format(Fore.WHITE, Fore.RED) + TaskList['Priority'])
                elif TaskList['Priority'] == "medium":
                    print("{}Priority:{} ".format(Fore.WHITE, Fore.YELLOW) + "Medium")
                elif TaskList['Priority'] == "Low":
                    print("{}Priority:{} ".format(Fore.WHITE, Fore.BLUE) + TaskList['Priority'])
                elif TaskList['Priority'] == "Unknown":
                    print("{}Priority:{} ".format(Fore.WHITE, Fore.MAGENTA) + TaskList['Priority'])
                print("{}Due date: ".format(Fore.WHITE) + TaskList['Time'])
        elif int(choice) == 3:
            name = input("Type task name: ")
            with open(filename, "r") as f:
                pseudotasklist = json.load(f)
            if name in pseudotasklist:
                pseudotasklist.pop(name)
                with open(filename, "w",) as f:
                    json.dump(pseudotasklist, f, indent=4)
            else:
                print("Error 3: Name dont exist!")
        elif int(choice) == 4:
            print("_________")
            print("{}Credits:{} ".format(Fore.LIGHTBLUE_EX, Fore.WHITE))
            print("{}Program -{} SUMER".format(Fore.LIGHTCYAN_EX, Fore.WHITE))
            print("{}Color console -{} Colorama (https://pypi.org/project/colorama/)".format(Fore.LIGHTGREEN_EX, Fore.WHITE))
            print("{}Code lang - {}Python{}".format(Fore.YELLOW, Fore.LIGHTCYAN_EX, Fore.WHITE))
            print("{}License -{} GNU Affero General Public License v3".format(Fore.MAGENTA, Fore.WHITE))
            print("_________")
        else:
            print("Error 2: Invalid command!")
    else:
        print("Error 1: You type text!")
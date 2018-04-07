"""Diary for a single user to add, edit, delete and view entries"""

# create user input, append, add, delete, view diary as date, or between selection of dates

import numpy as np

calender = np.load('diary.npy').item()

welcome = input("Enter name: ")


def userinput(): 

    action = input("What would you like to do %s? \n A: Add entry \n B: Append entry \n C: Delete entry \n D: View entry \n E: Exit \n Please enter: "  % (welcome))

    if action.lower() == "a":
        entry_date = input("Please enter date you would like to create entry to. \n Date should be entered in the following format 'dd/mm/yyyy' \n " )
        if len(entry_date) != 10:
            print("Wrong, please try again")
            entry_date
        else:
            new_entry = input("Please enter new entry: " )
            print(new_entry)
            save = input("Save entry? Y/N: " )
            if save.lower() == 'y':
                calender[entry_date] = new_entry
            else:
                return ("Cancelled")


    elif action.lower() == "b":
        entry_date = input("Please enter date you would like to append. \n Date should be entered in the following format 'dd/mm/yyyy' \n " )

        if len(entry_date) != 10:
            print("Wrong, please try again")
            return (entry_date)
        else:
            if entry_date in calender:
                print (calender)
                append = input("Please append entry: ")
                print(append)
                save = input("Save entry? Y/N: " )
                if save.lower() == 'y':
                    calender[entry_date] = append 
                else:
                    return ("Cancelled")
            else:
                print ("No entry at this date")

    elif action.lower() == 'c':
        entry_date = input("Please enter the date you would like to delete.\n Date should be entered in the following format 'dd/mm/yyyy' \n " )
        if len(entry_date) != 10:
            print("Wrong, please try again")
            return (entry_date)
        else:
            if entry_date not in calender:
                print("No entry exists")
            else:
                print(calender)
                check = input("Are you sure you want to delete? ")
                if check.lower() == 'y':
                    del calender[entry_date]
                else:
                    return

    elif action.lower() == "d":
        entry_date = input("Please enter the date you would like to view. \n Date should be entered in the following format 'dd/mm/yyyy' \n " )
        if len(entry_date) != 10:
            print("Wrong, please try again")
            return (entry_date)
        else:
            if entry_date in calender:
                print(calender[entry_date])

    elif action.lower() == 'e':
            return                 

    else:
        print ('\n Error. Please try again')
        userinput()

userinput()

def contin():
    cont = input("Would you like to carry on? Y/N: ")
    if cont.lower() == 'y':
        userinput()
    else:
        return

contin()

np.save('diary.npy', calender) 


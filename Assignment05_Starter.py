# ---------------------------------------------------------------------------------------------------------------------#
# Title: Assignment05_Starter.py
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# Change Log: (Who, When, What)
# LValderrama, 2021-07-22, Created File
# LValderrama, 2021-07-25, Modified the script to capture user input
# LValderrama, 2021-08-01, Modified the script to enable removing tasks from list and corrected saving to txt file "bug"
# ---------------------------------------------------------------------------------------------------------------------#

# Objective:
# The Assignment05.py script is designed to:
# 1. Manage a .txt file named "ToDo.txt" that contains two columns of data, "Task" and "Priority."
# 2. Load the columns into a Python Dictionary object. Each dictionary object represents one row of data,
# and these rows must be added to a Python List object to create a table of data.

# -- Data -- #
# declare variables and constants
strChoice = ""  # A Capture the user option selection
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strFile = "ToDoList.txt"  # A row of text data from the file
objFile = None  # An object that represents a file
strMenu = ""  # A menu of user options

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
lstTable = []
objFile = open(strFile, "r")  # open the text file and read the data
for row in objFile:  # when the data returns
     lstRow = row.split(",")  # split the data into a list
     dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}  # put in the keys and extract values
     lstTable.append(dicRow)  # append to the table itself
objFile.close()  # closing the file is best practice

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
     Menu of Options
     1) Show current tasks
     2) Add a new task
     3) Remove an existing task
     4) Save data to file
     5) Exit program
     """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # Process the data
        print("******* The current items ToDo are: *******")
        for objRow in lstTable:  # Displaying rows below in the form of a vertical list
            print(objRow["Task"] + ',' + objRow["Priority"])  # Unpacking
        print("*******************************************")
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("\nType a Task and Priority")

        # Get user input
        Task = str(input("Enter a New Task: ")).strip()  # User enters task by way of input function
        Priority = str(input("Enter Priority (Top, Med, Low): ")).strip()  # User enters task by way of input function
        dicRow = {"Task": Task, "Priority": Priority}  # Build new dictionary row
        lstTable.append(dicRow)  # the lstTable is appended with data added by the user
        print('\nYour Current Tasks are:')
        for objRow in lstTable:
            print(objRow["Task"] + ',' + objRow["Priority"])  # Unpacking the data entered by user
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        while len(lstTable) > 0:
            print("Current Task list:\n", "\n".join([f"\t{item['Task']}" for item in lstTable]))  # Display current data
            term = input("Type the Task you want to delete or type 'exit' to return to Menu of Options: ")
            if term.lower() == "exit":  # Option for the user to exit the while len loop
                break
            for task in lstTable:
                if term in task["Task"]:  # If the task entered by the user matches the name in the list then proceed
                    print(f"Removing {task['Task']}...")  # Print a message "item found" and processing removal
                    lstTable.remove(task)  # The item is removed from the table
                    break
            else:
                print(f"Task not found in list: {term}")  # Displays message indicating the task was not found!
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        print('\nWould you like to save your data?')
        strSaveToFileInput = input("Enter 'y' or 'n': ")
        if (strSaveToFileInput == 'n'):  # Conditional number 1 which will not save data to txt file
            print('Data not saved!')
        if (strSaveToFileInput == 'y'):  # Conditional number 2 which will save data to txt file
            # Process the data into file
            objFile = open(strFile, "w")  # "a" to append the file and not overwrite the exiting data
            for row in lstTable:
                objFile.write(row["Task"] + "," + row["Priority"] + "\n")  # Unpacking
            objFile.close()  # File close, best practice
            print('\nYour data is saved to:', strFile)
            continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Thank you!')
        EndProgram = input('\n(Press Enter to End Program)')
        break  # and Exit the program

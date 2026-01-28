# Let us code raw a to do list.

# Define a list
tdl = []

def show_list():
    print("---To-Do-List---")
    for index , task in enumerate(tdl):
        print(index, task)

while True:
    # Showing the Menu
    print("----MENU----")
    print("1. Add Task")
    print("2. Edit Tasks")
    print("3. Delete Task")
    print("4. Show Tasks")
    print("5. Quit")
    # User input
    choice = int(input("Enter your choice: "))
    if choice == 1:
        task = input("Enter the Task: ")
        tdl.append(task)
        print("Task added")
    elif choice == 2:
        if tdl:
            show_list()
            index = int(input("Select the index of the task: "))
            if 0 <= index < len(tdl):
                task = input("Enter the new task: ")
                tdl[index] = task
                print("Task edited successfully.")
            else:
                print("Invalid index")
        else:
            print("There are no tasks in the list.")
    elif choice == 3:
        if tdl:
            show_list()
            index = int(input("Enter the index of the task to be deleted: "))
            if 0 <= index < len(tdl):
                tdl.pop(index)
            else:
                print("Invalid index")
            print("Task deleted successfully")
        else:
            print("There are no tasks in the list.")
    elif choice == 4:
        if tdl:
            show_list()
        else:
            print("There are no tasks in the list.")
    elif choice == 5:
        break

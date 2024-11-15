##Created by Bryan Xaysanavongphet 11/14/2024
##Going off Shaun Halversons YT video
## https://www.youtube.com/watch?v=aEIHZDv_23U


tasks = []

#Creating a createTask function to enter a string into the array
def createTask():
    task = input("Please enter a task: ")
    #Adding the task to the array
    tasks.append(task)
    print(f"The task '{task}' has been added to the list.")

def deleteTask():
    #Listing the the whole list of tasks
    #listTask()
    try:
        taskToDelete = int(input("Enter the # of task to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            #using the .pop function to remove the input 
            tasks.pop(taskToDelete)
            print(f"Task #{taskToDelete} has been deleted.")
        else:
            #If the # was lower than 0 or if higher than the amount of tasks that are inputted.
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid input.")
        
def listTask():
    if not (tasks):
        print ("There are no tasks currently")
    else:
        print("\n")
        print("----------------------------------")
        print("Here are the current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")
        print("---------------------------------")
        print("\n")
        
        
if __name__ == "__main__":
    print("Welcome to the To-Do List!")
    while True:
        print("-----------------------------------")
        print("Please select a choice below.")
        print("1. Create a new task")
        print("2. Lists tasks")
        print("3. Delete task")
        print("4. Quit")
        
        choice = input("Please enter your choice: ")
    
    #Creating the if statements to call the functions that the user wants to access.
        if (choice == "1"):
            createTask()
        elif (choice == "2"):
            listTask()
        elif(choice == "3"):
            deleteTask()
        elif(choice == "4"):
            break
        else:
            print("Invalid input. Please try again.")

    print("Thank you for using the To Do list!")
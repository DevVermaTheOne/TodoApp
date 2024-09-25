"""an infinite loop that can be exit on users wish
user given options to choose from
options :
            add task
            remove task
            view task
            exit program"""


todos = [{"task": "a", "summary": "asdy", "status": "asdds"},
         {"task": "b", "summary": "asdy", "status": "asdds"},
         {"task": "c", "summary": "asdy", "status": "asdds"}] # stores all the todo tasks


def addTask():
    taskname = input("Enter task name ")
    tasksummary = input("Enter task summary ")
    taskstatus = input("Enter task status ")

    task = {"task": taskname, "summary": tasksummary, "status": taskstatus}
    todos.append(task)
    return 

def removeTask():
    for i, tasks in enumerate(todos) : print(i,":",tasks)
    taskid = int(input("input task_id of task that requires removal"))
    if taskid < len(todos):
        todos.pop(taskid)
    else:
        print("Invalid input")

def changeStatus():
    pass


while True:
    print("""Choose one of these options :
          1. add task
          2. remove task
          3. View task
          4. exit program """)
    
    choice = input("Enter the number corresponding to your choice ")

    match choice:
        case "1":
            addTask()

        case "2":
            removeTask()

        case "3":
            for i, tasks in enumerate(todos) : print(i,":",tasks)
            
        case "4":
            break
        
        case _:
            print("Invalid option. Please try again")
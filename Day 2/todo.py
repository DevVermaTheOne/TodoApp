import sqlite3

conn = sqlite3.connect("todoApp.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS todos(
          task_id INTEGER NOT NULL PRIMARY KEY,
          task TEXT,
          summary TEXT,
          completed INTEGER)""")
    
def addTask():
    taskname = input("Enter task name ")
    tasksummary = input("Enter task summary ")
    completed = 0

    task = {"task": taskname, "summary": tasksummary, "completed": completed}
    c.execute("INSERT INTO todos VALUES (null, :task, :summary, :completed)", (task))

    return 

def removeTask():
    c.execute("SELECT * FROM todos")
    for i in c.fetchall(): print(i)

    taskid = int(input("input task_id of task that requires removal"))

    # write exception for invalid inputs
    c.execute("""DELETE FROM todos
              WHERE task_id= :task_id""",({"task_id": taskid}))

def changeStatus():

    taskid = int(input("input task_id of task that requires status change"))
    # 0->1 and 1->0
    c.execute("""UPDATE todos
              SET completed = 1 - completed
              WHERE task_id = ?""",[taskid])

while True:
    print("""Choose one of these options :
          1. add task
          2. remove task
          3. View task
          4. change status
          5. exit program""")
    
    choice = input("Enter the number corresponding to your choice ")

    match choice:
        case "1":
            addTask()

        case "2":
            removeTask()

        case "3":
            c.execute("SELECT * FROM todos")
            for i in c.fetchall(): print(i) 
            
        case "4":
            changeStatus()
        
        case "5":
            exitchoice = (input("Are you sure you want to exit (y/n)?")).lower
            if exitchoice == 'y':
                break
        case _:
            print("Invalid option. Please try again")

conn.commit()
conn.close()
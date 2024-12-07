import sqlite3
from datetime import date
from os import system, name


today = str(date.today())   #get the today date

#SQL commands
selectByState = "SELECT rowid, nameTask, description, curState, createAt, updateAt FROM tasks WHERE curState = ?"
selectAll = "SELECT rowid, nameTask, description, curState, createAt, updateAt FROM tasks"
markIn = "UPDATE tasks SET curState = ?, updateAt = ? WHERE rowid = ?"
checkIfExists = "SELECT rowid FROM tasks WHERE rowid = ?"

def clearScreen():

    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def PrintTasks (result):

    print("============================== TASKS ===============================")

    if result:
        for row in result:
            print(f"Id: {row[0]} Task: {row[1]}")
            print(f"Description: {row[2]}")
            print(f"State: \"{row[3]}\" Create at: \"{row[4]}\" Update at: \"{row[5]}\"")
            print()

def ListByState (cursor, state):

    cursor.execute(selectByState, (state, ))
    result = cursor.fetchall() 
 
    if result:
        PrintTasks(result)

    else:
        print("Task Tracker > list is empty!")
        print()

def updateState (con, command):

    try:
        idTask = commands.pop(0)

        match idTask:

            case idTask if idTask.isdigit():
                
                result = con.execute("SELECT rowid FROM tasks WHERE rowid = ?", (idTask, ))

                if result.fetchone() is not None:
                    con.execute(markIn, (command, today, idTask))
                    print(f"Task Tracker > task id {idTask} is {command}!")
                    
                else:
                    print("Task Tracker > id task not found!")

            case _:
                print("Task Tracker > command invalid, insert a valid id!")
    except IndexError:
        print("Task Tracker > command invalid!")

    print()

def executeCommand (commands):

    con = sqlite3.connect("tasks.db")
    cursor = con.cursor()

    res = con.execute("SELECT name FROM sqlite_master WHERE TYPE = 'table'")

    if res.fetchone() is None:
        con.execute("CREATE TABLE tasks(nameTask, description, curState, createAt, updateAt)")

    currentCommand = commands.pop(0)

    match currentCommand:
        case "add":
            
            if len(commands) > 0:

                taskName = " ".join(str(element) for element in commands)

                print("Task Tracker > Give a description about the task")
                description = input("Task Tracker > ")
                   
                con.execute("INSERT INTO tasks VALUES(?, ?, ?, ?, ?)", (taskName, description, "to-do", today, ""))
                
            else:
                print("Task Tracker > insert a name task!")

            print()
            
        case "list":

            if commands:
                currentCommand = commands.pop(0)
                
                cursor.execute(selectAll)
                result = cursor.fetchall()

                if result:

                    match currentCommand:
                        case "all":
                            PrintTasks(result)
                            
                        case "in-progress":
                            ListByState(cursor, currentCommand)

                        case "to-do":
                            ListByState(cursor, currentCommand)

                        case "done":
                            ListByState(cursor, currentCommand)
                        
                        case _:
                            print("Task Tracker > invalid command!")

                else:
                    print("Task Tracker > list is empty!")
                    print()

            else:
                print("Task Tracker > use list all, todo, in-progress or done")
                print()

        case "update":
          
            try:
                
                idTask = commands.pop(0)

                match idTask:

                    case idTask if idTask.isdigit():

                        result = con.execute(checkIfExists, (idTask, ))

                        if result.fetchone() is not None:

                            taskName = " ".join(str(element) for element in commands)

                            if taskName:
                                con.execute("UPDATE tasks SET nameTask = ? WHERE rowid = ?", (taskName, idTask))
                                print("task name was updated!")
                            else:
                                print("Task Tracker > task name can't be blank")
                        
                        else:
                            print("Task Tracker > id task not found!")

                    case _:
                        print("Task Tracker > insert a valid id!")
            
            except IndexError:
                print("Task Tracker > pass an id task!")

            print()

        case "delete":

            if commands:
                idTask = commands.pop(0)

                match idTask:
                    case "all":
                        con.execute("DELETE FROM tasks")
                        print("Task Tracker > all tasks was deleted!")

                    case idTask if idTask.isdigit():

                        result = con.execute("SELECT rowid FROM tasks WHERE rowid = ?", (idTask, ))

                        if result.fetchone() is not None:
                            con.execute("DELETE FROM tasks WHERE rowid = ?", (idTask,))
                            print(f"Task Tracker > task id {idTask} was deleted!")
                        
                        else:
                            print("Task Tracker > id task not found!")

                    case _:
                        print("Task Tracker > invalid command!")
                    
            else:
                print("Task Tracker > Use delete all or pass an task id")

            print("")

        case "mark-in-progress":
            updateState(con, "in-progress")

        case "mark-in-done":
            updateState(con, "done")

        case "quit":
            global isRunning
            isRunning = False
            print("Task Tracker > Thanks for use it! :)")

        case "clear":
            clearScreen()

    con.commit()
    con.close()
    commands.clear()

clearScreen()

isRunning = True

while isRunning:

    cli = input("Task Tracker > ")
    commands = cli.split(" ")

    executeCommand(commands)


    

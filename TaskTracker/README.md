# CLI TASK TRACKER

Light, simple and easy to use it. Written in python 3 and using Sqlite3 to store data,
this incredible project offer you an amazing CLI task tracker with just what you need.
Add, list, delete, rename and keep track of your tasks progress

## Usage

To use it, just clone the repo and run Python/TaskTracker/TaskTracker.py
```
$ git clone https://github.com/d4alencar/Python
```
```
$ cd Python/TaskTracker
```
```
$ python TaskTracker.py
```
## Commands

insert a new task in the database.
```
add taskname
```

list all tasks or by progress situation.
this command prints task id, name, description, progress, creation and update date.
```
list all
list to-do
list in-progress
list done
```

delete all task created or a specific one passing their ID.
```
delete all
delete idTask
```

update progress of a task.
```
mark-in-progress idTask
mark-in-done idTask
```

rename a task.
```
update idTask newName
```

clear screen.
```
clear
```

stop the script.
```
quit
```

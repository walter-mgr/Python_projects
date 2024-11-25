# When we start the programm we can see this To-Do list menu:
#    1. View Tasks
#    2. Add a Task
#    3. Remove a Task
#    4. Exit
# Enter your choice: choose from the given 4 options
# After each choice we have to see Todo list menu

# 1. View Tasks:
#   if list is empty We get a message: "No tasks in the list"
#   otherwise: print a list of tasks
#       // for index, task in enumerate(tasks, 1):
#              -> index, task

# 2. Add a task
#   1. Get a message: "Enter a new task"
#       if input not a string: print Error message /.lower().strip()
#   2. Store added tasks in the database (define datastructure)

# 3. Remove the task
#   1. Get a message: "Enter the task number: " // only int(task number)
#       if not an int from range of tasks:
#           Error message

todo = {
    "menu": ["View Tasks", "Add a Task", "Remove a Task", "Exit"],
    "tasks": [],
}
print(todo["menu"])

from termcolor import cprint, colored

REMOVE_ALL = "0"
VIEW_TASKS = "1"
ADD_TASK = "2"
REMOVE_TASK = "3"
EXIT = "4"


def print_menu(menu):
    cprint("\nMENU", "cyan", attrs=["reverse"])
    for value in menu:
        print(value)


def print_no_task():
    cprint("\nNo tasks in the list", "yellow")


def view_tasks(tasks):
    if not tasks:
        print_no_task()
        return
    cprint("\nTO-DO LIST", "cyan", attrs=["reverse"])
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")


def get_task() -> str:
    while True:
        try:
            task = input(colored("\nEnter a task: ", "yellow")).capitalize().strip()
            if not task:
                raise ValueError()
            return task
        except ValueError:
            cprint("Enter a text", "red")


def get_user_input(tasks) -> int:
    while True:
        try:
            choice = int(input(colored("\nEnter a Task number: ", "green")))
            if 0 < choice <= len(tasks):
                return choice
            raise ValueError()
        except ValueError:
            cprint("Invalid input", "red")


def get_menu_coice() -> str:
    valid_choices = (REMOVE_ALL, VIEW_TASKS, ADD_TASK, REMOVE_TASK, EXIT)
    while True:
        try:
            menu_choice = input(colored("\nEnter your choice: ", "green"))
            if menu_choice in valid_choices:
                return menu_choice
            raise ValueError()
        except ValueError:
            cprint("Choose from the given options", "red")


def add_task(tasks, task):
    tasks.append(task)


def remove_task(tasks):
    if not tasks:
        print_no_task()
    else:
        view_tasks(tasks)
        user_input = get_user_input(tasks)
        tasks.pop(user_input - 1)


def main():
    menu = ["1. View Tasks", "2. Add Task", "3. Remove Task", "4. Exit"]
    tasks = []

    while True:
        print_menu(menu)

        menu_choice = get_menu_coice()
        if menu_choice == VIEW_TASKS:
            view_tasks(tasks)

        elif menu_choice == ADD_TASK:
            task = get_task()
            add_task(tasks, task)

        elif menu_choice == REMOVE_TASK:
            # view_tasks(tasks)
            remove_task(tasks)

        elif menu_choice == EXIT:
            break


if __name__ == "__main__":
    main()

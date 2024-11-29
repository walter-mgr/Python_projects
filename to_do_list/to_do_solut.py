from termcolor import cprint, colored
from enum import Enum


class MenuOption(Enum):
    VIEW_TASKS = "1"
    ADD_TASK = "2"
    REMOVE_TASK = "3"
    EXIT = "4"


REMOVE_ALL = "0"
CYAN = "cyan"
MAGENTA = "magenta"
YELLOW = "yellow"
GREEN = "green"


def print_menu(menu: list) -> None:
    """
    Prints the menu to the console
    """
    cprint("\nMENU", CYAN, attrs=["reverse"])
    for item in menu:
        print(item)


def print_no_task() -> None:
    """Prints a message indicating there are no tasks"""
    cprint("\nNo tasks in the list", YELLOW)


def view_tasks(tasks: list) -> None:
    """Prints the list of tasks"""
    if not tasks:
        print_no_task()
        return
    cprint("\nTO-DO LIST", CYAN, attrs=["reverse"])
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")


def get_task() -> str:
    """Prompts the user to enter a task"""
    while True:
        try:
            task = input(colored("\nEnter a task: ", YELLOW)).capitalize().strip()
            if task:
                return task
            raise ValueError()
        except ValueError:
            cprint("Enter a text", "red")


def get_valid_user_input(tasks: list) -> int:
    """Gets a valid task number from the user"""
    while True:
        try:
            choice = int(input(colored("\nEnter a Task number: ", GREEN)))
            if 0 < choice <= len(tasks):
                return choice
            raise ValueError()
        except ValueError:
            cprint("Invalid input", "red")


def get_menu_choice() -> MenuOption:
    """Gets a valid menu choice from the user"""
    valid_choices = [option.value for option in MenuOption]
    while True:
        try:
            menu_choice = input(colored("\nEnter your choice: ", GREEN))
            if menu_choice in valid_choices:
                return MenuOption(menu_choice)
            raise ValueError()
        except ValueError:
            cprint("Choose from the given options", MAGENTA)


def add_task(tasks: list, task: str) -> None:
    "Adds a task to the list of tasks"
    tasks.append(task)


def remove_task(tasks: list) -> None:
    """Removes a task from the list o tasks"""
    if not tasks:
        print_no_task()
        return

    view_tasks(tasks)

    user_input = get_valid_user_input(tasks)
    tasks.pop(user_input - 1)


def remove_all_tasks(tasks):
    """Prompts to remove all tasks if there are more than one task in the list"""
    if len(tasks) > 1:
        view_tasks(tasks)
        choice = input(
            colored("To delete all press '0'. To continue press any: ", MAGENTA)
        ).strip()

        if choice == REMOVE_ALL:
            tasks.clear()
            return


def handle_menu_choice(menu_choice, tasks):
    """Handles the user menu choice"""
    if menu_choice == MenuOption.VIEW_TASKS:
        view_tasks(tasks)

    elif menu_choice == MenuOption.ADD_TASK:
        task = get_task()
        add_task(tasks, task)

    elif menu_choice == MenuOption.REMOVE_TASK:
        remove_all_tasks(tasks)
        remove_task(tasks)


def main():
    """Runs To-Do List application"""
    menu = ["1. View Tasks", "2. Add Task", "3. Remove Task", "4. Exit"]
    tasks = []

    while True:
        print_menu(menu)
        menu_choice = get_menu_choice()

        if menu_choice == MenuOption.EXIT:
            break

        handle_menu_choice(menu_choice, tasks)


if __name__ == "__main__":
    main()

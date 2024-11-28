from termcolor import cprint, colored


HEADERS = "headers"
MENU = "menu"
TASKS = "tasks"
PROMPTS = "prompts"

todo = {
    HEADERS: ["MENU", "TASKS"],
    MENU: ["View Tasks", "Add a Task", "Remove a Task", "Exit"],
    TASKS: [],
    PROMPTS: [
        "Enter your choice: ",
        "Enter the task number: ",
        "Enter a new task: ",
    ],
}


def print_header(header, color="cyan"):
    cprint(header, color, attrs=["reverse"])


def display_menu(todo):
    print_header(todo[HEADERS][0])
    for index, menu in enumerate(todo[MENU], 1):
        print(f"{index}. {menu}")


def get_user_choice(prompt, array) -> int:
    while True:
        try:
            choice = int(input(colored(prompt, "green")))
            print()
            if choice <= 0 or choice > len(array):
                raise ValueError()
            return choice
        except ValueError:
            cprint("Please, choose a number from the given options", "red")


def get_task(prompt) -> str:
    while True:
        try:
            task = input(colored(prompt, "yellow")).strip().capitalize()
            if not task:
                raise ValueError()
            return task
        except ValueError:
            cprint("Enter a text", "magenta")


def print_no_tasks():
    cprint("No tasks in the list", "yellow")
    print()


def remove_task(todo, choice):
    if not todo[TASKS]:
        print_no_tasks()
    else:
        choice = get_user_choice(todo[PROMPTS][1], todo[TASKS])
        todo[TASKS].pop(choice - 1)


def view_tasks(todo):
    if todo[TASKS]:
        print_header(todo[HEADERS][1])
        for index, task in enumerate(todo[TASKS], 1):
            print(f"{index}. {task}")
        print()

    else:
        print_no_tasks()


def main():
    while True:
        display_menu(todo)

        choice = get_user_choice(todo[PROMPTS][0], todo[MENU])
        if choice == 1:
            view_tasks(todo)

        elif choice == 2:
            task = get_task(todo[PROMPTS][2])
            todo[TASKS].append(task)

        elif choice == 3:
            view_tasks(todo)
            remove_task(todo, choice)

        else:
            break


if __name__ == "__main__":
    main()

from termcolor import cprint

A = (1, 1)
B = (1, 2)
C = (1, 3)
D = (2, 1)
E = (2, 2)
F = (2, 3)
G = (3, 1)
H = (3, 2)
I = (3, 3)

grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


cells = [A, B, C, D, E, F, G, H, I]


def print_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)


lable = ["row", "column"]


def player_move(lable):
    choices = (1, 2, 3)
    while True:
        try:
            move = int(input(f"Select {lable} (1-3): "))
            if move in choices:
                return move
            else:
                raise ValueError()
        except ValueError:
            cprint("Wrong input", "red")


def define_cell():
    select_row = player_move(lable[0])
    select_column = player_move(lable[1])
    cell = (select_row, select_column)
    return cell


# TODO: define condition for game exit
player = ("X", "0")


def define_winner(value):
    winner = ""
    if (
        (grid[0][0] == value and grid[1][1] == value and grid[2][2] == value)
        or (grid[0][2] == value and grid[1][1] == value and grid[2][0] == value)
        or (grid[0][0] == value and grid[0][1] == value and grid[0][2] == value)
        or (grid[1][0] == value and grid[1][1] == value and grid[1][2] == value)
        or (grid[2][0] == value and grid[2][1] == value and grid[2][2] == value)
        or (grid[0][0] == value and grid[1][0] == value and grid[2][0] == value)
        or (grid[0][1] == value and grid[1][1] == value and grid[2][1] == value)
        or (grid[0][2] == value and grid[1][2] == value and grid[2][2] == value)
    ):
        winner = f"Player {value} is the Winer!"
    return winner


def x_player_move():
    while len(cells):
        cprint(f"X's player turn", "blue")
        try:
            x_move = define_cell()
            if x_move in cells:
                grid[x_move[0] - 1][x_move[1] - 1] = player[0]
                cells.remove(x_move)
                print_grid(grid)
                # break
                o_player_move()
            else:
                raise ValueError()
        except ValueError:
            cprint("This spot is busy!", "yellow")


def o_player_move():
    while len(cells):
        cprint(f"0's player turn", "blue")
        try:
            o_move = define_cell()
            if o_move in cells:
                grid[o_move[0] - 1][o_move[1] - 1] = player[1]
                cells.remove(o_move)
                print_grid(grid)

                x_player_move()
            else:
                raise ValueError()
        except ValueError:
            cprint("This spot is busy!", "yellow")


def main():
    x_player_move()
    o_player_move()


main()

# coordinates = [{"row": (1, 2, 3)}, {"column": (1, 2, 3)}]


"""
def print_grid():
    for i in range(3):
        print("---+---+---")
        print(f" {' '} |" * 2 + f" {' '}")
"""


A = (0, 0)
B = (0, 1)
C = (0, 2)
D = (1, 0)
E = (1, 1)
F = (1, 2)
G = (2, 0)
H = (2, 1)
I = (2, 2)

grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

cells = [A, B, C, D, E, F, G, H, I]
# print(cells)
# cells.remove(C)
# print(cells)


def print_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)


# take coordinates from PLAYER_1
lable = ["row", "column"]


def player_move(lable):
    choices = (0, 1, 2)
    while True:
        try:
            move = int(input(f"Select {lable} (0-2): "))
            if move in choices:
                return move
            else:
                raise ValueError()
        except ValueError:
            print("Wrong input")


def define_cell():
    select_row = player_move(lable[0])
    select_column = player_move(lable[1])
    cell = (select_row, select_column)
    return cell


# TODO: define condition for game exit
# TODO: after X, move X again is not allowed


def x_player_move():
    while len(cells):
        print(f"X's player turn")
        try:
            x_move = define_cell()
            if x_move in cells:
                grid[x_move[0]][x_move[1]] = "X"
                cells.remove(x_move)
                print_grid(grid)
                print(cells)
                print(len(cells))
                o_player_move()
            else:
                raise ValueError()
        except ValueError:
            print("This spot is busy!")


def o_player_move():
    while len(cells):
        print(f"0's player turn")
        try:
            o_move = define_cell()
            if o_move in cells:
                grid[o_move[0]][o_move[1]] = "0"
                cells.remove(o_move)
                print_grid(grid)
                print(cells)
                print(len(cells))
                x_player_move()
            else:
                raise ValueError()
        except ValueError:
            print("This spot is busy!")


def main():
    x_player_move()
    o_player_move()


main()

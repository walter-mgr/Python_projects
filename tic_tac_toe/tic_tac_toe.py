coordinates = [{"row": (1, 2, 3)}, {"column": (1, 2, 3)}]


"""
def print_grid():
    for i in range(3):
        print("---+---+---")
        print(f" {' '} |" * 2 + f" {' '}")
"""


grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
A = (0, 0)
B = (0, 1)
C = (0, 2)
D = (1, 0)
E = (1, 1)
F = (1, 2)
G = (2, 0)
H = (2, 1)
I = (2, 2)


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


first_player = define_cell()
second_player = define_cell()
print(first_player)
print(second_player)


"""
busy = []
first_player_move = player_move()
if first_player_move == A:
    grid[0][0] = "X"
    busy.append(A)
    print_grid(grid)
    print(busy)


second_player_move = player_move()
if second_player_move == B:
    grid[0][1] = "0"
    busy.append(B)
    print_grid(grid)
    print(busy)
elif second_player_move in busy:
    print("This spot is occupied")
    second_player_move = player_move()
    if second_player_move == B:
        grid[0][1] = "0"
        busy.append(B)
    print_grid(grid)
    print(busy)
"""

# if second_player_move == (1, 1):
# grid[1][1] = "0"
# print_grid(grid)


# grid[1][2] = "0"
# grid[0][2] = "X"

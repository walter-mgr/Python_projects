from termcolor import cprint

# Cells coordinates
A = (1, 1)
B = (1, 2)
C = (1, 3)
D = (2, 1)
E = (2, 2)
F = (2, 3)
G = (3, 1)
H = (3, 2)
I = (3, 3)

# Table structure
grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


cells = [A, B, C, D, E, F, G, H, I]
row_or_column = ("row", "column")
players = ("X", "0")


def print_grid(grid):
    print("-" * 9)
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)


def get_user_input(row_or_column: int) -> int:
    choices = (1, 2, 3)
    while True:
        try:
            move = int(input(f"Select {row_or_column} (1-3): "))
            if move in choices:
                return move
            else:
                raise ValueError()
        except ValueError:
            cprint("Invalid input", "red")


def define_cell():
    select_row = get_user_input(row_or_column[0])
    select_column = get_user_input(row_or_column[1])
    cell = (select_row, select_column)
    return cell


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
        winner = value
        cprint(f"Player {winner} is the Winner!", "green")

    return winner


def player_move(players):
    while len(cells):
        cprint(f"{players}'s player turn", "blue")
        try:
            move = define_cell()
            if move in cells:
                grid[move[0] - 1][move[1] - 1] = players
                cells.remove(move)
                print_grid(grid)
                return players
            else:
                raise ValueError()
        except ValueError:
            cprint("This spot is alredy taken!", "yellow")


def main():
    while len(cells):

        player_1 = player_move(players[0])
        winner = define_winner(player_1)
        if winner == player_1:
            break

        else:
            player_2 = player_move(players[1])
            winner = define_winner(player_2)
            if winner == player_2:
                break


main()

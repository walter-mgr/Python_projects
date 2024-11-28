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
    line = "-" * 9
    print(line)
    for row in grid:
        print(" | ".join(row))
        print(line)


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
            cprint("This spot is already taken!", "yellow")


def determine_winner(player):
    for index, row in enumerate(grid):
        column = [row[index] for row in grid]
        if (
            (grid[0][0] == grid[1][1] == grid[2][2] == player)
            or (grid[0][2] == grid[1][1] == grid[2][0] == player)
            or (row[0] == row[1] == row[2] == player)
            or (column[0] == column[1] == column[2] == player)
        ):
            winner = player
            return winner


def main():
    winner = None
    while not winner:

        for player in players:
            player = player_move(player)
            winner = determine_winner(player)

            if winner:
                cprint(f"Player {winner} is winner", "green")
                break

        if not winner and not len(cells):
            cprint("No winner was declared. It's a tie!", "light_magenta")
            break


if __name__ == "__main__":
    main()

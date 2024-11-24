from termcolor import cprint


board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
row_column = ("row", "column")


def print_board(board):
    line = "-" * 9
    print(line)
    for row in board:
        print(" | ".join(row))
        print(line)


def get_player_input(row_column):
    options = (1, 2, 3)
    while True:
        try:
            move = int(input(f"Select {row_column} (1-3): "))
            if move in options:
                return move
            else:
                raise ValueError()
        except ValueError:
            cprint("Invalid input", "red")


def get_cell():
    row = get_player_input(row_column[0])
    column = get_player_input(row_column[1])
    cell = [row, column]
    return cell


def is_empty(board, cell, current_player):
    if board[cell[0] - 1][cell[1] - 1] != " ":
        return False
    else:
        board[cell[0] - 1][cell[1] - 1] = current_player
        return True


def check_winner(board, current_player):
    for index, row in enumerate(board):
        column = [row[index] for row in board]
        if (
            (row[0] == row[1] == row[2] == current_player)
            or (column[0] == column[1] == column[2] == current_player)
            or (board[0][0] == board[1][1] == board[2][2] == current_player)
            or (board[0][2] == board[1][1] == board[2][0] == current_player)
        ):
            return True


def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def main():
    current_player = "X"
    while True:

        cprint(f"{current_player}'s player turn", "blue")

        cell = get_cell()

        if is_empty(board, cell, current_player):
            print_board(board)
        else:
            cprint("This spot is already taken, try again", "yellow")
            continue

        if check_winner(board, current_player):
            cprint(f"Player {current_player} is a winner!", "green")
            break

        if is_full(board):
            cprint("The board is full. No winner was detected", "light_magenta")
            break

        current_player = "0" if current_player == "X" else "X"


if __name__ == "__main__":
    main()

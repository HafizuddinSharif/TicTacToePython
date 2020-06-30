# TO DISPLAY THE GAME BOARD
def display_board(marker_positions):
    for x in range(3):
        if x != 0:
            print("-------------")
        print("  " + marker_positions[x * 3] + " | " + marker_positions[(x * 3) + 1] + " | " + marker_positions[(x * 3) + 2] + "  ")


# TO INSERT THE SYMBOL IN THE POSITIONS
def insert_symbol(player, selected_coordinate, marker_positions):
    if selected_coordinate == 0:
        return False

    if player == "X":
        marker_positions[selected_coordinate - 1] = "X"
    else:
        marker_positions[selected_coordinate - 1] = "O"

    return True


# TO CHECK IF SOMEONE WINS
def is_win(player, marker_positions):
    # HORIZONTAL
    for x in range(3):
        if marker_positions[x * 3] == player:
            if marker_positions[x * 3 + 1] == player and marker_positions[x * 3 + 2] == player:
                return True

    # VERTICAL
    for x in range(3):
        if marker_positions[x] == player:
            if marker_positions[x + 3] == player and marker_positions[x + 6] == player:
                return True

    # DIAGONAL
    if marker_positions[0] == player:
        if marker_positions[4] == player and marker_positions[8] == player:
            return True
    if marker_positions[6] == player:
        if marker_positions[4] == player and marker_positions[2] == player:
            return True

    return False


# TO CHECK IF IT IS A DRAW
def is_draw(marker_positions):
    for x in marker_positions:
        if x == " ":
            return False
    return True


# THE INTERFACE TO START THE GAME
def start_game(start_first, initial_positions):
    turn = start_first
    current_positions = initial_positions
    won = False

    while not won:
        display_board(current_positions)

        coordinate = int(input(turn + " player, please type in your coordinate:\n"))
        insert_symbol(turn, coordinate, current_positions)

        if is_win(turn, current_positions):
            won = True
            display_board(current_positions)
            print(turn + " player WINS")
        elif is_draw(current_positions):
            won = True
            display_board(current_positions)
            print("Its a DRAW")
        else:
            turn = "O" if turn == "X" else "X"


# GAME SET UP
positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
start_game("X", positions)

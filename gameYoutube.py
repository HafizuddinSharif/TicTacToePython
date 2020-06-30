# Untuk menunjukkan keadaan permainan
def display_board(positions):
    for x in range(3):
        print(" " + positions[x*3] + " | " + positions[(x*3) + 1] + " | " + positions[(x*3) +2] + " ")
        if x != 2:
            print("-----------")


# Membolehkan pemain untuk meletakkan simbol mereka
def insert_symbol(player, positions):

    coordinate = int(input())
    if player == "X":
        positions[coordinate-1] = "X"
    elif player == "O":
        positions[coordinate-1] = "O"


# Untuk memeriksa adakah pemain itu menang atau tidak
def is_win(player, positions):

    # HORIZONTAL
    for x in range(3):
        if positions[x*3] == player:
            if positions[x*3 + 1] == player and positions[x*3 + 2] == player:
                return True

    # VERTICAL
    for x in range(3):
        if positions[x] == player:
            if positions[x + 3] == player and positions[x + 6] == player:
                return True

    # DIAGONAL
    if positions[0] == player:
        if positions[4] == player and positions[8] == player:
            return True
    if positions[6] == player:
        if positions[4] == player and positions[2] == player:
            return True

    return False


# Untuk memeriksa adakah permainan seri
def is_draw(positions):
    for symbol in positions:
        if symbol == " ":
            return False

    return True


# Function untuk memulakan permainan
def start_game(player, initial_positions):

    turn = player
    won = False
    curr_positions = initial_positions

    while not won:
        display_board(curr_positions)

        print(turn + " please enter your coordinate:")
        insert_symbol(turn, curr_positions)

        if is_win(turn, curr_positions):
            display_board(curr_positions)
            print(turn + " won the game")
            won = True
            break
        elif is_draw(curr_positions):
            display_board(curr_positions)
            print("Is is a draw")
            won = True
            break
        else:
            if turn == "X":
                turn = "O"
            else:
                turn = "X"


# Game dimulakan di sini
current_positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
start_game("X", current_positions)


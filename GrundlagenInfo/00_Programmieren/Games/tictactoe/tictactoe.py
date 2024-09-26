def print_board(board, n):
    print((2 * n + 1) * "#")
    i = 0
    while i < n:
        j = 0
        row = ""
        while j < n:
            row += "|" + board[i * n + j]

            j += 1

        print(row + "|")
        i += 1

    print((2 * n + 1) * "#")


def check_win(board, n, token):
    winning_pattern = n * token
    # check rows
    for i in range(n):
        row = ""
        for j in range(n):
            row += board[i * n + j]
        if row == winning_pattern:
            return True

    # check columns
    for j in range(n):
        column = ""
        for i in range(n):
            column += board[i * n + j]
        if column == winning_pattern:
            return True

    # check diagonals
    diag = ""
    for i in range(n):
        diag += board[i * n + i]
    if diag == winning_pattern:
        return True
    diag = ""
    for i in range(n):
        diag += board[i * n + (n - 1) - i]
    if diag == winning_pattern:
        return True

    return False


def play(n):
    empty_token = "-"
    A_token = "X"
    B_token = "O"
    player = "A"
    board = n * n * [empty_token]

    # print("board layout:\n")
    # L = []
    # k = 1
    # while k <= n * n:
    #     L.append(str(k))
    #     k += 1
    # print_board(L, n)
    # print("\n")

    print_board(board, n)
    print("\n")

    token_count = 0
    while token_count < n * n:
        if token_count % 2 == 0:
            player = "A"
            token = A_token
        else:
            player = "B"
            token = B_token

        move = int(input(player + " wo möchtest Du Dein Token setzen?\n")) - 1
        while board[move] != empty_token:
            print("Das Feld", move + 1, "ist bereits besetzt")
            move = int(input(player + " bitte wähle ein unbesetztes Feld:\n")) - 1

        board[move] = token
        print_board(board, n)
        if check_win(board, n, token):
            print(player, "has won the game!")
            return

        token_count += 1

    print("unentschieden!")
    return


play(3)

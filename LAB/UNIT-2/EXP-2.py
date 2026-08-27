board = [' '] * 9

def show():
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])

def win(p):
    for a, b, c in [(0,1,2),(3,4,5),(6,7,8),
                    (0,3,6),(1,4,7),(2,5,8),
                    (0,4,8),(2,4,6)]:
        if board[a] == board[b] == board[c] == p:
            return True
    return False

for turn in range(9):
    show()
    p = 'X' if turn % 2 == 0 else 'O'
    pos = int(input(f"Player {p}, enter position (1-9): ")) - 1

    if board[pos] == ' ':
        board[pos] = p
    else:
        print("Position already occupied!")
        continue

    if win(p):
        show()
        print("Player", p, "wins!")
        break
else:
    show()
    print("It's a draw!")

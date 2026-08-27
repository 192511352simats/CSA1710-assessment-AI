board = [' '] * 9

def win(p):
    for a,b,c in [(0,1,2),(3,4,5),(6,7,8),
                  (0,3,6),(1,4,7),(2,5,8),
                  (0,4,8),(2,4,6)]:
        if board[a] == board[b] == board[c] == p:
            return True
    return False

def minimax(is_max):
    if win('O'): return 1
    if win('X'): return -1
    if ' ' not in board: return 0

    scores = []
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' if is_max else 'X'
            scores.append(minimax(not is_max))
            board[i] = ' '
    return max(scores) if is_max else min(scores)

def best_move():
    best = -2
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best:
                best, move = score, i
    return move

for turn in range(9):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

    if turn % 2 == 0:
        pos = int(input("Enter your position (1-9): ")) - 1
        board[pos] = 'X'
        if win('X'):
            print("You win!")
            break
    else:
        pos = best_move()
        board[pos] = 'O'
        print("Computer chose:", pos + 1)
        if win('O'):
            print("Computer wins!")
            break
else:
    print("Draw!")

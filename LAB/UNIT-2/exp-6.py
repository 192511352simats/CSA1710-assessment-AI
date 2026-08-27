def minimax(depth, node, alpha, beta, maximizing):
    if depth == 3:
        return values[node]

    if maximizing:
        best = -999
        for i in range(2):
            best = max(best, minimax(depth + 1, node * 2 + i,
                                     alpha, beta, False))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 999
        for i in range(2):
            best = min(best, minimax(depth + 1, node * 2 + i,
                                     alpha, beta, True))
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


n = int(input("Enter number of leaf values: "))
values = []

for i in range(n):
    values.append(int(input(f"Enter value {i + 1}: ")))

print("Best value:", minimax(0, 0, -999, 999, True))

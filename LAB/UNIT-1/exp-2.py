N = 8
b = [-1] * N

def safe(r, c):
    for i in range(c):
        if b[i] == r or abs(b[i] - r) == abs(i - c):
            return False
    return True

def solve(c):
    if c == N:
        print("Solution:")
        for i in range(N):
            for j in range(N):
                print("Q" if b[j] == i else ".", end=" ")
            print()
        return True

    for r in range(N):
        if safe(r, c):
            b[c] = r
            if solve(c + 1):
                return True
            b[c] = -1   

    return False

solve(0)

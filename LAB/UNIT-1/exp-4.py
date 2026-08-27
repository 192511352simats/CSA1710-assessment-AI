from collections import deque
def valid(m, c):
    return (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c)
def bfs():
    q = deque([((3, 3, 1), [])])
    visited = set()

    while q:
        (m, c, b), path = q.popleft()

        if (m, c, b) in visited:
            continue
        visited.add((m, c, b))
        path = path + [(m, c, b)]

        if (m, c) == (0, 0):
            return path

        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

        for dm, dc in moves:
            if b:
                nm, nc, nb = m - dm, c - dc, 0
            else:
                nm, nc, nb = m + dm, c + dc, 1

            if 0 <= nm <= 3 and 0 <= nc <= 3 and valid(nm, nc):
                q.append(((nm, nc, nb), path))

for state in bfs():
    print(state)

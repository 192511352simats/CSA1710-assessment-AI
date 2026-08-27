from itertools import permutations

n = int(input("Enter number of cities: "))
cost = [list(map(int, input().split())) for _ in range(n)]

min_cost = float('inf')
best_path = ()

for p in permutations(range(1, n)):
    path = (0,) + p + (0,)
    c = sum(cost[path[i]][path[i+1]] for i in range(n))
    if c < min_cost:
        min_cost = c
        best_path = path

print("Shortest Path:", " -> ".join(map(str, best_path)))
print("Minimum Cost:", min_cost)

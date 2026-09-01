import random

n = int(input("Enter population size: "))
g = int(input("Enter generations: "))

pop = [random.randint(0, 31) for _ in range(n)]

for _ in range(g):
    pop.sort(key=lambda x: x*x, reverse=True)
    pop = pop[:n//2]
    while len(pop) < n:
        p = random.choice(pop)
        c = p ^ (1 << random.randint(0, 4))
        pop.append(c)

best = max(pop, key=lambda x: x*x)
print("Best x:", best)
print("Maximum value:", best*best)

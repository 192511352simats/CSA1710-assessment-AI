import random

X = [(0,0),(0,1),(1,0),(1,1)]
Y = [0,1,1,0]

def fitness(w):
    score = 0
    for (a,b), y in zip(X,Y):
        out = 1 if w[0]*a + w[1]*b + w[2] > 0 else 0
        score += out == y
    return score

pop = [[random.uniform(-2,2) for _ in range(3)] for _ in range(20)]

for _ in range(100):
    pop.sort(key=fitness, reverse=True)
    pop = pop[:10]
    while len(pop) < 20:
        p = random.choice(pop).copy()
        i = random.randrange(3)
        p[i] += random.uniform(-1,1)
        pop.append(p)

best = max(pop, key=fitness)
print("Best weights:", best)
print("Fitness:", fitness(best), "/ 4")

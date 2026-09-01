import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

n = int(input("Enter number of users: "))
m = int(input("Enter number of items: "))

R = []

for i in range(n):
    R.append(list(map(int, input("Enter ratings: ").split())))

R = np.array(R)
sim = cosine_similarity(R)

u = int(input("Enter user number: ")) - 1
similar = np.argsort(sim[u])[-2]

unrated = np.where(R[u] == 0)[0]

print("Recommended items:")
for i in unrated:
    if R[similar][i] > 0:
        print("Item", i + 1)

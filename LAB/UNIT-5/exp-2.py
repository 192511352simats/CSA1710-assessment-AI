import random

states = input("Enter states: ").split()
n = int(input("Enter number of transitions: "))

T = {}

for s in states:
    T[s] = input(f"Transitions from {s}: ").split()

current = input("Enter starting state: ")

print("Sequence:", current, end=" ")

for _ in range(n):
    current = random.choice(T[current])
    print(current, end=" ")

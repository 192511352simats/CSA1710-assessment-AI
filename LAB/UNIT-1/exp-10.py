from itertools import permutations

w1 = input("First Word: ").upper()
w2 = input("Second Word: ").upper()
res = input("Result Word: ").upper()

letters = "".join(set(w1 + w2 + res))

for p in permutations("0123456789", len(letters)):
    d = dict(zip(letters, p))

    if d[w1[0]] == '0' or d[w2[0]] == '0' or d[res[0]] == '0':
        continue

    n1 = int("".join(d[i] for i in w1))
    n2 = int("".join(d[i] for i in w2))
    n3 = int("".join(d[i] for i in res))

    if n1 + n2 == n3:
        print(w1, "=", n1)
        print(w2, "=", n2)
        print(res, "=", n3)
        break

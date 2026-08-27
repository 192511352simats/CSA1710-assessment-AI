cap1 = int(input("Enter capacity of Jug 1: "))
cap2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target: "))

a = b = 0

print((a, b))

while a != target and b != target:
    if a == 0:
        a = cap1
    elif b == cap2:
        b = 0
    else:
        t = min(a, cap2 - b)
        a -= t
        b += t

    print((a, b))

print("Target reached!")

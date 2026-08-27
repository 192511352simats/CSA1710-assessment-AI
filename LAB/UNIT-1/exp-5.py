# Vacuum Cleaner Problem
left = input("Enter Left Room (Dirty/Clean): ").lower()
right = input("Enter Right Room (Dirty/Clean): ").lower()
pos = input("Enter Vacuum Position (Left/Right): ").lower()

if pos == "left":
    if left == "dirty":
        print("Clean Left")
    if right == "dirty":
        print("Move Right")
        print("Clean Right")
else:
    if right == "dirty":
        print("Clean Right")
    if left == "dirty":
        print("Move Left")
        print("Clean Left")

print("Goal State Reached")

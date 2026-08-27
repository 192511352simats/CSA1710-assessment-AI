graph = eval(input("Enter graph: "))
heuristic = eval(input("Enter heuristic values: "))
start = input("Enter start node: ")
goal = input("Enter goal node: ")

open_list = [(start, 0, [start])]
visited = set()

while open_list:
    open_list.sort(key=lambda x: x[1] + heuristic[x[0]])
    node, cost, path = open_list.pop(0)

    if node == goal:
        print("Path:", " -> ".join(path))
        print("Total Cost:", cost)
        break

    if node not in visited:
        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                open_list.append((neighbor, cost + weight, path + [neighbor]))
else:
    print("Goal not found")

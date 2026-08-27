def color_map(graph, colors):
    result = {}

    def solve(node):
        if node == len(graph):
            return True

        for c in colors:
            if all(result.get(n) != c for n in graph[node]):
                result[node] = c
                if solve(node + 1):
                    return True
                del result[node]
        return False

    return result if solve(0) else None


n = int(input("Enter number of regions: "))

graph = {}
for i in range(n):
    graph[i] = list(map(int, input(
        f"Enter adjacent regions for {i} (space separated): "
    ).split()))

colors = input("Enter colors (space separated): ").split()

solution = color_map(graph, colors)

if solution:
    print("\nMap Coloring:")
    for region, color in solution.items():
        print("Region", region, ":", color)
else:
    print("No solution possible")

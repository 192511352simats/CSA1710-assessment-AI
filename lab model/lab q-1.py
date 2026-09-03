from itertools import permutations

def tsp_brute_force(distance, cities):
    start = cities[0]
    min_distance = float('inf')
    best_path = None

    # Generate all permutations except the starting city
    for perm in permutations(cities[1:]):
        path = (start,) + perm + (start,)
        total_distance = 0

        # Calculate total distance
        for i in range(len(path) - 1):
            total_distance += distance[path[i]][path[i + 1]]

        # Find shortest path
        if total_distance < min_distance:
            min_distance = total_distance
            best_path = path

    return best_path, min_distance


# Cities
cities = ['A', 'B', 'C', 'D']

# Distance matrix
distance = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

best_path, shortest_distance = tsp_brute_force(distance, cities)

print("Shortest Path:", best_path)
print("Shortest Distance:", shortest_distance)

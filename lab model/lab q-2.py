# Tree represented using a dictionary
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J'],
    'F': ['K', 'L'],
    'G': ['M']
}

def dfs(node, goal, visited):
    print(node, end=" ")

    if node == goal:
        return True

    visited.add(node)

    for child in tree.get(node, []):
        if child not in visited:
            if dfs(child, goal, visited):
                return True

    return False


print("DFS Traversal:")
visited = set()

if dfs('A', 'L', visited):
    print("\nGoal node L found.")
else:
    print("\nGoal node L not found.")

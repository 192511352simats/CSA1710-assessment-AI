from collections import deque

graph = {}

n = int(input("Enter the number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex: ")
    neighbors = input("Enter adjacent vertices (space-separated): ").split()
    graph[vertex] = neighbors

start = input("Enter the starting vertex: ")

visited = set()
queue = deque([start])

print("BFS Traversal:")

while queue:
    vertex = queue.popleft()

    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)

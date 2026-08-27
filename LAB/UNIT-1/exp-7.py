graph = eval(input("Enter graph: "))
start = input("Enter starting node: ")
visited = set()
def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for i in graph[node]:
            dfs(i)
dfs(start)

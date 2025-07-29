def bfs(graph, start_node):
    visited = []
    queue = [None] * 100
    front = 0
    rear = 0

    queue[rear] = start_node
    rear += 1
    visited += [start_node]

    print("Following is the Breadth-First Search:")

    while front < rear:
        current = queue[front]
        front += 1
        print(current, end=" ")

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited += [neighbor]
                queue[rear] = neighbor
                rear += 1

# User input for the graph
graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node label: ")
    neighbors = input(f"Enter neighbors of {node} separated by spaces: ").split()
    graph[node] = neighbors

start_node = input("Enter the starting node: ")
bfs(graph, start_node)

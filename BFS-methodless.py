graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

def bfs(graph, start):
    visited = []
    queue = [None] * 100
    front = 0
    rear = 0

    queue[rear] = start
    rear += 1
    visited += [start]

    print("Following is the Breadth-First Search:")

    while front < rear:
        node = queue[front]
        front += 1
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited += [neighbour]
                queue[rear] = neighbour
                rear += 1

bfs(graph, '5')

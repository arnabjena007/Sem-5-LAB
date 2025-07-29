from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

# Example usage
graph = {
    0: [1, 2],
    1: [3],
    2: [4],
    3: [],
    4: []
}

print(bfs(graph, 0))

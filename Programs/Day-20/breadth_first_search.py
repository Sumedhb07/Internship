from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current == goal:
            print(f"Goal node '{goal}' found!")
            return True  # Or return the path if tracking it
        if current not in visited:
            print(f"Visiting: {current}")
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    print("Goal not found.")
    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs(graph, 'A', 'E')

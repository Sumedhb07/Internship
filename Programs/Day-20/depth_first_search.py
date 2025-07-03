def dfs_recursive(graph, current, goal, visited=None):
    if visited is None:
        visited = set()

    print(f"Visiting: {current}")
    if current == goal:
        print(f"Goal node {goal} found!")
        return True

    visited.add(current)

    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            found = dfs_recursive(graph, neighbor, goal, visited)
            if found:
                return True  # stop once goal is found

    return False  # goal not found in this path

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

start_node = 'A'
goal_node = 'G'

dfs_recursive(graph, start_node, goal_node)

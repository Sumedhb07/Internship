#  2. DFS Implementation (Path - Not necessarily shortest)
# python
# CopyEdit
def dfs_path(graph, start, goal):
    visited = set()
    stack = [[start]]  # Stack stores paths

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph.get(node, [])):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return None
# Best-First Search(Graph, start, goal):
#     1. Initialize the open list with the start node
#     2. Initialize the closed list as empty
#     3. While the open list is not empty:
#         a. Select the node n from open list with lowest heuristic h(n)
#         b. If n is the goal node:
#             return the path from start to n
#         c. Remove n from open list
#         d. Add n to closed list
#         e. For each neighbor m of n:
#             If m is not in open list and not in closed list:
#                 Set parent of m to n
#                 Add m to open list
#     4. Return failure (goal not found)

import heapq

def best_first_search(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    came_from = {}  # For reconstructing path
    closed_set = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return path[::-1]

        closed_set.add(current)

        for neighbor in graph[current]:
            if neighbor not in closed_set and neighbor not in [node for _, node in open_list]:
                came_from[neighbor] = current
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))

    return None  # If goal not found
# Example usage

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 7,
    'E': 2,
    'F': 3,
    'G': 0
}

path = best_first_search(graph, 'A', 'G', heuristic)
print("Path found:", path)



# function GreedyBestFirstSearch(start, goal):
#     open_list ← priority queue ordered by h(n)
#     open_list.push(start)
#     came_from ← empty map
#     visited ← empty set

#     while open_list is not empty:
#         current ← open_list.pop()

#         if current == goal:
#             return reconstruct_path(came_from, current)

#         add current to visited

#         for each neighbor of current:
#             if neighbor not in visited:
#                 came_from[neighbor] ← current
#                 open_list.push(neighbor)

#     return failure


import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    came_from = {}
    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))

    return None  # failure

def reconstruct_path(came_from, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    return path

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': ['F'], 'F': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 3,
    'F': 0
}

path = greedy_best_first_search(graph, 'A', 'F', heuristic)
print("Path:", path)

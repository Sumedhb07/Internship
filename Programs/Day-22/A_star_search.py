# function A_Star(start, goal):
#     open_list ← priority queue containing start node with f(start)
#     came_from ← empty map
#     g_score[start] ← 0
#     f_score[start] ← h(start)

#     while open_list is not empty:
#         current ← node in open_list with lowest f_score

#         if current == goal:
#             return reconstruct_path(came_from, current)

#         remove current from open_list

#         for each neighbor of current:
#             tentative_g_score ← g_score[current] + cost(current, neighbor)

#             if tentative_g_score < g_score[neighbor]:
#                 came_from[neighbor] ← current
#                 g_score[neighbor] ← tentative_g_score
#                 f_score[neighbor] ← g_score[neighbor] + h(neighbor)

#                 if neighbor not in open_list:
#                     add neighbor to open_list with priority f_score[neighbor]

#     return failure


import heapq

def a_star(start, goal, graph, h):
    open_list = []
    heapq.heappush(open_list, (0 + h(start), start))  # (f(n), node)

    came_from = {}
    g_score = {start: 0}

    while open_list:
        f_current, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, cost in graph.get(current, []):
            tentative_g = g_score[current] + cost

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + h(neighbor)
                heapq.heappush(open_list, (f_score, neighbor))

    return None  # Failure

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]  # reverse the path

# Graph is represented as an adjacency list: node -> list of (neighbor, cost)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic dictionary
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 3,
    'F': 4,
    'G': 0
}

# Heuristic function (replacing lambda)
def h(n):
    return heuristic[n]

# Run A* algorithm
path = a_star('A', 'G', graph, h)
print("Path:", path)


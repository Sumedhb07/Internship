#1. Greedy Best-First Search (GBFS)
import heapq
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def greedy_best_first_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    heap = [(manhattan(start, goal), start)]
    came_from = {start: None}
    nodes_explored = 0

    while heap:
        _, current = heapq.heappop(heap)
        nodes_explored += 1

        if current == goal:
            break

        if current in visited:
            continue
        visited.add(current)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited:
                    heapq.heappush(heap, (manhattan(neighbor, goal), neighbor))
                    if neighbor not in came_from:
                        came_from[neighbor] = current

    # Reconstruct path
    path = []
    curr = goal
    while curr and curr in came_from:
        path.append(curr)
        curr = came_from[curr]
    path.reverse()

    return path, nodes_explored
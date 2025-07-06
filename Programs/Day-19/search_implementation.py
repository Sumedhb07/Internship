# 2. A* Search Implementation
# python
# CopyEdit
def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    heap = [(manhattan(start, goal), 0, start)]
    came_from = {start: None}
    g_cost = {start: 0}
    nodes_explored = 0

    while heap:
        _, cost_so_far, current = heapq.heappop(heap)
        nodes_explored += 1

        if current == goal:
            break

        if current in visited:
            continue
        visited.add(current)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 0:
                    new_g = g_cost[current] + 1
                    if neighbor not in g_cost or new_g < g_cost[neighbor]:
                        g_cost[neighbor] = new_g
                        f_cost = new_g + manhattan(neighbor, goal)
                        heapq.heappush(heap, (f_cost, new_g, neighbor))
                        came_from[neighbor] = current

    # Reconstruct path
    path = []
    curr = goal
    while curr and curr in came_from:
        path.append(curr)
        curr = came_from[curr]
    path.reverse()

    return path, nodes_explored
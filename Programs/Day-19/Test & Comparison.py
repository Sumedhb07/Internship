#  3. Test and Comparison
# python
# CopyEdit
grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

gbfs_path, gbfs_nodes = greedy_best_first_search(grid, start, goal)
a_star_path, a_star_nodes = a_star_search(grid, start, goal)
print("Greedy BFS Path:", gbfs_path)
print("Greedy BFS Nodes Explored:", gbfs_nodes)
print("A* Path:", a_star_path)
print("A* Nodes Explored:", a_star_nodes)

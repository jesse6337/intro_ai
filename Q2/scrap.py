world_map = [[0,0,1,0,0,0],
        [0,0,1,0,0,0],
        [0,0,0,0,1,0],
        [0,0,1,1,1,0],
        [0,0,0,0,1,0]]

cost_grid = [[0 for j in range(len(world_map[i]))] for i in range(len(world_map))]
print(cost_grid)
#create function 
def search(world_map, start, goal):
    
    directions = ['^', '<', 'v', '>']
#define possible movements (up down left right)
    moves = [[-1, 0],
             [0, -1],
             [1, 0],
             [0, 1]]
#set defult condition 
    found = False
#define stating xy position 
    r = start[0]
    c = start[1]
#count useful info like number 0f movemets
    move_cost = 0
    expansion_count = 0
#prevent moving backwards
    open_paths = [[r, c]]
    closed_paths = []
# creates grids and set all positions = 0
    cost_grid = [['X' for i in range(len(world_map[j]))] for j in range(len(world_map))]
    cost_grid[r][c]=0

    expansion_grid = [['X' for i in range(len(world_map[j]))] for j in range(len(world_map))]
    expansion_grid[r][c] = 0

    # define an action_grid
    # each cell will become the index of the move from moves that got you there
    action_grid = [['X' for i in range(len(world_map[j]))] for j in range(len(world_map))]
#runs untill everything is finished
    while not found:

        temp_open_paths = []
#counter
        move_cost += 1

        for i in range(len(open_paths)):
            #check next open path
            current_pos = open_paths[i]
            #mark path as closed for later
            closed_paths.append(current_pos)
            # x y compents
            r = current_pos[0]
            c = current_pos[1]
            #move in all directions
            for j in range(len(moves)):

                newr = r + moves[j][0]
                newc = c + moves[j][1]
                # create upper and lower bounds r
                if newr >= 0 and newr <= len(world_map) - 1:
                    # create upper and lower bounds c
                    if newc >= 0 and newc <= len(world_map[0]) - 1:
                        #checks if clear
                        if world_map[newr][newc] == 0:
                            #not allow closed paths
                            if [newr, newc] not in closed_paths:
                                # not already checked
                                if [newr, newc] not in temp_open_paths:
                                    # add to path
                                    temp_open_paths.append([newr, newc])
                                    #counter
                                    expansion_count += 1
                                    #update cost and expantion grids
                                    cost_grid[newr][newc] = move_cost
                                    expansion_grid[newr][newc] = expansion_count

                                    # set each position in action grid to be the move that got you there
                                    action_grid[newr][newc] = j
        #copy path list
        open_paths = temp_open_paths.copy()
        #end condition
        if goal in open_paths:
            found = True
    #returns all grids
    path = action_grid.copy()
    for i in range(len(world_map)-1, -1, -1):
        for j in range(len(world_map[1])-1, -1, -1):
            try:path[i][j] = directions[action_grid[i][j]]
            except:path[i][j] = "X"
        
    return world_map, action_grid

# *********************************************************** #
############## DO NOT MODIFY ANYTHING BELOW THIS ##############
############## DO NOT MODIFY ANYTHING BELOW THIS ##############
# *********************************************************** #
# dispaly graph list
def show_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(str(grid[i][j]).ljust(2), end=' ')
        print()

#expamples
# Test Case 1
world1 = [[0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 1, 0],
          [0, 0, 1, 1, 1, 0],
          [0, 0, 0, 0, 1, 0]]

start1 = [0, 0]
goal1 = [4, 5]

# Test Case 2
world2 = [[0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 1, 0],
          [0, 0, 1, 0, 1, 0],
          [0, 0, 1, 0, 1, 0]]

start2 = [4, 0]
goal2 = [3, 3]

# Test Case 3
world3 = [[0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 1, 0],
          [0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 1, 0],
          [0, 0, 0, 0, 1, 0]]

start3 = [4, 5]
goal3 = [0, 0]

# Running all test cases
cases = ((world1, start1, goal1), (world2, start2, goal2), (world3, start3, goal3))
test_case = 1

for i in range(len(cases)):
    print(f'TEST CASE {test_case} RESULTS:')
    test_world = cases[i][0]
    test_start = cases[i][1]
    test_end = cases[i][2]
    results = search(test_world, test_start, test_end)
    for j in range(len(results)):
        show_grid(results[j])
        print()
    test_case += 1

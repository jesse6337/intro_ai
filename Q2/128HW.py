############## DIRECTIONS ##############
# Complete the program below by filling in code to below each comment you see
# The code you fill in below each comment can be as many lines as you would like and...
# ...it should do what the comment describes. You should not delete any of the code below.
# You should only need to add to this program.


def search(world_map, start, goal):

    directions = ['^', '<', 'v', '>']

    moves = [[-1, 0],
             [0, -1],
             [1, 0],
             [0, 1]]
    move_cost = [3,1,2,1]

    found = False

    r = start[0]
    c = start[1]

    # create a variable to track the movement cost for each move
    # create a variable track the expansion step for each expansion
    step = 0

    open_paths = [[r, c]]
    closed_paths = []

    # create a temporary 2D array called cost_grid (mirrors the world map)
    # each cell will become the movement cost amount to get there
    cost_grid = [[0 for j in range(len(world_map[0]))] for i in range(len(world_map))]
    # set the starting position to have a cost of 0
    total_cost = 0

    # create a temporary 2D array called expansion_grid (mirrors the world map)
    # each cell will become the expansion step number
    expansion_grid = [[0 for j in range(len(world_map[0]))] for i in range(len(world_map))]
    # set the starting position to have an expansion step number of 0
    expansions = 0

    while not found:

        temp_open_paths = []

        # increasing the move cost value by 1

        for i in range(len(open_paths)):

            current_pos = open_paths[i]
            closed_paths.append(current_pos)
            r = current_pos[0]
            c = current_pos[1]

            for j in range(len(moves)):

                newr = r + moves[j][0]
                newc = c + moves[j][1]

                if newr >= 0 and newr <= len(world_map) - 1:

                    if newc >= 0 and newc <= len(world_map[0]) - 1:

                        if world_map[newr][newc] == 0:

                            if [newr, newc] not in closed_paths:

                                if [newr, newc] not in temp_open_paths:
                                    temp_open_paths.append([newr, newc])
                                    total_cost += move_cost[j]
                                    # increasing the move cost value by 1
                                    expansions +=1
                                    # set the value of the cell in cost_grid to be the current cost amount
                                    cost_grid[newr][newc] = total_cost

                                    # set the value of the cell in expansion_grid to be the current expansion amount
                                    expansion_grid[newr][newc] = expansions

        open_paths = temp_open_paths.copy()
        if goal in open_paths:
            found = True

    # return the cost and expansion grid
    return cost_grid, expansion_grid


# *********************************************************** #
############## DO NOT MODIFY ANYTHING BELOW THIS ##############
############## DO NOT MODIFY ANYTHING BELOW THIS ##############
# *********************************************************** #

def show_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(str(grid[i][j]).ljust(2), end=' ')
        print()


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
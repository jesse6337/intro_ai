world = [[0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 1, 1, 1, 0],
         [0, 0, 0, 0, 1, 0]]

start = [0, 0]
end = [4, 5]

moves = [[-1, 0],
         [0, -1],
         [1, 0],
         [0, 1]]

found = False

r = start[0]
c = start[1]

open_paths = [[r, c]]

print(open_paths)

closed_paths = []

while not found:

    temp_open_paths = []

    for i in range(len(open_paths)):

        current_pos = open_paths[i]
        closed_paths.append(current_pos)
        r = current_pos[0]
        c = current_pos[1]

        for j in range(len(moves)):

            newr = r + moves[j][0]
            newc = c + moves[j][1]

            if newr >= 0 and newr <= len(world) - 1:

                if newc >= 0 and newc <= len(world[0]) - 1:

                    if world[newr][newc] == 0:

                        if [newr, newc] not in closed_paths:

                            if [newr, newc] not in temp_open_paths:
                                temp_open_paths.append([newr, newc])

    open_paths = temp_open_paths.copy()
    print(open_paths)
    if end in open_paths:
        found = True
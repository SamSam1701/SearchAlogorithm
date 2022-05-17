import main

def solve_maze_DFS(maze, start, end):
    # We use a Python list as a stack - then we have push operations as append, and pop as pop.
    cost = 0
    stack = [start]
    explored = []
    dfsPath = {}

    # Go through the stack as long as there are elements
    while len(stack) > 0:
        curcell = stack.pop()
        pos_r, pos_c = curcell

        if pos_r==end[0] and pos_c == end[1]:
            break

        if maze[pos_r][pos_c] == '*':
            continue

        # Mark position as visited
        maze[pos_r][pos_c] = '*'

        # Check for all possible positions and add if possible
        if main.is_valid_position(maze, pos_r - 1, pos_c):
            childcell = (pos_r - 1, pos_c)
            if childcell not in explored:
                stack.append(childcell)
                explored.append(childcell)
                dfsPath[childcell] = curcell


        if main.is_valid_position(maze, pos_r + 1, pos_c):
            childcell = (pos_r + 1, pos_c)
            if childcell not in explored:
                stack.append(childcell)
                explored.append(childcell)
                dfsPath[childcell] = curcell


        if main.is_valid_position(maze, pos_r, pos_c - 1):
            childcell = (pos_r, pos_c-1)
            if childcell not in explored:
                stack.append(childcell)
                explored.append(childcell)
                dfsPath[childcell] = curcell


        if main.is_valid_position(maze, pos_r, pos_c + 1):
            childcell = (pos_r, pos_c+1)
            if childcell not in explored:
                stack.append(childcell)
                explored.append(childcell)
                dfsPath[childcell] = curcell

    cost = len(explored)
    fwdpath = {}
    cell = end
    while cell!=start:
        fwdpath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return fwdpath, cost

import main
from queue import PriorityQueue

def  heuristic (cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2 
    return abs(x1 - x2) + abs (y1 - y2)

def Astar (matrix, start, end):
    cost = 0
    walls=[(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j]==' ' or matrix[i][j]=='+']
    g_score = {cell:float('inf') for cell in walls}
    g_score[start] = 0
    f_score = {cell:float('inf') for cell in walls}
    f_score[start] = heuristic(start, end)

    open = PriorityQueue()
    open.put((heuristic(start,end), heuristic(start, end),start))
    aPath = {}
    while not open.empty():
        curcell = open.get()[2]
        pos_r, pos_c = curcell
        if curcell == end:
            break
        
        if main.is_valid_position(matrix, pos_r - 1, pos_c):
            childCell = (pos_r - 1, pos_c)
            temp_g_score = g_score[curcell]+1
            temp_f_score = temp_g_score + heuristic(childCell, end)
            
            if temp_f_score < f_score[childCell]:
                g_score[childCell] = temp_g_score
                f_score[childCell] = temp_f_score
                open.put((temp_f_score,heuristic(childCell, end),childCell))
                aPath[childCell] = curcell
                cost +=1
        
        if main.is_valid_position(matrix, pos_r + 1, pos_c):
            childCell = (pos_r + 1, pos_c)
            temp_g_score = g_score[curcell]+1
            temp_f_score = temp_g_score + heuristic(childCell, end)

            if temp_f_score < f_score[childCell]:
                g_score[childCell] = temp_g_score
                f_score[childCell] = temp_f_score
                open.put((temp_f_score,heuristic(childCell, end),childCell))
                aPath[childCell] = curcell
                cost +=1

        if main.is_valid_position(matrix, pos_r, pos_c-1):
            childCell = (pos_r, pos_c-1)
            temp_g_score = g_score[curcell]+1
            temp_f_score = temp_g_score + heuristic(childCell, end)

            if temp_f_score < f_score[childCell]:
                g_score[childCell] = temp_g_score
                f_score[childCell] = temp_f_score
                open.put((temp_f_score,heuristic(childCell, end),childCell))
                aPath[childCell] = curcell
                cost +=1

        if main.is_valid_position(matrix, pos_r, pos_c+1):
            childCell = (pos_r, pos_c+1)
            temp_g_score = g_score[curcell]+1
            temp_f_score = temp_g_score + heuristic(childCell, end)
            
            if temp_f_score < f_score[childCell]:
                g_score[childCell] = temp_g_score
                f_score[childCell] = temp_f_score
                open.put((temp_f_score,heuristic(childCell, end),childCell))
                aPath[childCell] = curcell
                cost +=1

    fwdPath={}
    cell = end
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    return fwdPath, cost


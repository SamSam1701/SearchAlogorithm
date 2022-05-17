import main
import math
from queue import PriorityQueue

def find_distance(cell1, cell2):
    x,y = cell1
    x1,y1 = cell2
    return math.sqrt(pow(x1-x,2)+pow(y1-y,2))

def Greedy_Search(matrix, start,end):
    cost = 0
    open = PriorityQueue()
    open.put(start)
    visitCell = []
    distanceCell = []
    aPath = {}

    while not open.empty():
        curcell = open.get()
        pos_r, pos_c = curcell
        if curcell == end:
            break
        
        if main.is_valid_position(matrix, pos_r - 1, pos_c):
            childCell_Up = (pos_r - 1, pos_c)
            if childCell_Up not in visitCell:
                visitCell.append(childCell_Up)
                distanceCell.append(find_distance(childCell_Up, end))
            
        if main.is_valid_position(matrix, pos_r + 1, pos_c):
            childCell_Down = (pos_r + 1, pos_c)
            if childCell_Down not in visitCell:
                visitCell.append(childCell_Down)
                distanceCell.append(find_distance(childCell_Down, end))

        if main.is_valid_position(matrix, pos_r, pos_c-1):
            childCell_Left = (pos_r, pos_c-1)
            if childCell_Left not in visitCell:
                visitCell.append(childCell_Left)
                distanceCell.append(find_distance(childCell_Left, end))

        if main.is_valid_position(matrix, pos_r, pos_c+1):
            childCell_Right = (pos_r, pos_c+1)
            if childCell_Right not in visitCell:
                visitCell.append(childCell_Right)
                distanceCell.append(find_distance(childCell_Right, end))
        
        min_distance = min(distanceCell)
        for i in range(0, len(visitCell)):
            if min_distance == find_distance(visitCell[i], end):
                open.put(visitCell[i])
                aPath[visitCell[i]] = curcell
                break
 
    cost = len(visitCell)
    fwdPath={}
    cell = end
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    return fwdPath, cost


import matplotlib.pyplot as plt
import DFS
import BFS
import Greedy
import AStar

def visualize_maze(matrix, bonus, start, end, route=None):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """
    #1. Define walls and array of direction based on the route
    walls=[(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j]=='x']

    if route:
        direction=[]
        for i in range(1,len(route)):
            if route[i][0]-route[i-1][0]>0:
                direction.append('^') #^
            elif route[i][0]-route[i-1][0]<0:
                direction.append('v') #v        
            elif route[i][1]-route[i-1][1]>0:
                direction.append('<')
            else:
                direction.append('>')

        #direction.pop(0)

    #2. Drawing the map
    ax=plt.figure(dpi=100).add_subplot(111)

    for i in ['top','bottom','right','left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls],[-i[0] for i in walls],
                marker='X',s=100,color='black')
    
    plt.scatter([i[1] for i in bonus],[-i[0] for i in bonus],
                marker='P',s=100,color='green')

    plt.scatter(start[1],-start[0],marker='*',
                s=100,color='gold')

    if route:
        for i in range(len(route)-2):
            plt.scatter(route[i+1][1],-route[i+1][0],
                        marker=direction[i],color='silver')

    plt.text(end[1],-end[0],'EXIT',color='red',
         horizontalalignment='center',
         verticalalignment='center')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    for _, point in enumerate(bonus):
      print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')



def read_file(file_name: str = 'maze.txt'):
    f=open(file_name,'r')
    n_bonus_points = int(next(f)[:-1])
    bonus_points = []
    for i in range(n_bonus_points):
        x, y, reward = map(int, next(f)[:-1].split(' '))
        bonus_points.append((x, y, reward))

    text=f.read()
    matrix=[list(i) for i in text.splitlines()]
    f.close()

    return bonus_points, matrix


def print_maze(maze):
    for row in maze:
        for item in row:
            print(item, end='')
        print()

from time import sleep


# This is only a helper function to see if we have a valid positino.
def is_valid_position(maze, pos_r, pos_c):
    if pos_r < 0 or pos_c < 0:
        return False
    if pos_r >= len(maze) or pos_c >= len(maze[0]):
        return False
    if maze[pos_r][pos_c] == "x":
        return False
    return True

def find_start_end (matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='S':
                start=(i,j)

            elif matrix[i][j]==' ':
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    end=(i,j)
                
            else:
                pass
    return start, end

bonus_points, matrix = read_file('kiểm thử\maze_map1.txt')
start, end = find_start_end(matrix)


def main():
    algo = input('Nhap thuat toan: ')
    if 'bfs' in algo:
        route_BFS = []
        BFS_PATH, cost = BFS.solve_maze_BFS(matrix,start,end)
        for item in BFS_PATH:
            route_BFS.append(item)
        route_BFS.insert(0, end)
        visualize_maze(matrix,bonus_points,start,end,route_BFS)
        print('Chi phi thuc hien BFS: ', cost)

    elif 'dfs' in algo:
        route_DFS = []
        DFS_PATH, cost = DFS.solve_maze_DFS(matrix,start,end)
        for item in DFS_PATH:
            route_DFS.append(item)
        route_DFS.insert(0, end)
        visualize_maze(matrix,bonus_points,start,end,route_DFS)
        print('Chi phi thuc hien DFS: ', cost)

    elif 'greedy' in algo:
        route_Greedy = []
        Greedy_PATH, cost  = Greedy.Greedy_Search(matrix,start,end)
        for item in Greedy_PATH:
            route_Greedy.append(item)
        route_Greedy.insert(0, end)
        visualize_maze(matrix,bonus_points,start,end,route_Greedy)
        print('Chi phi thuc hien Greedy: ', cost)

    elif 'astar' in algo:
        route_Astar = []
        AStar_PATH,cost= AStar.Astar(matrix, start,end)
        for item in AStar_PATH:
            route_Astar.append(item)
        route_Astar.insert(0,end)
        visualize_maze(matrix,bonus_points,start,end,route_Astar)
        print('Chi phi thuc hien Astar: ', cost)
        

    else:
        print('Nhap lai thuat toan!!')
if __name__=='__main__':
    main()


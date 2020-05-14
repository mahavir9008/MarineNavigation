M = 202 # Rows
N = 229 # Columns
def isSafe(grid,visited,x,y):
    if grid[x][y]=='0' or visited[x][y]==True:
        return False # Unsafe
    return True # Safe

def isValid(x,y):
    if x<M and y<N and x>=0 and y>=0:
        return True # Valid
    return False # Invalid

def solve(grid,visited,i,j,dest_x,dest_y,curr_dist,min_dist,shortestPath,currentPath):
    if i==dest_x and j==dest_y: # if destination is found, update min_dist
        if curr_dist<min_dist[0]: # If a shorter distance is found
            min_dist[0] = curr_dist # Update distance
            shortestPath.clear() # Update path
            shortestPath.extend(currentPath)
            shortestPath.append((dest_y,dest_x)) # Push the destination coordinates
        return

    # set (i, j) cell as visited
    visited[i][j] = True
    currentPath.append((j,i))

    # go to bottom cell
    if isValid(i + 1, j) and isSafe(grid,visited,i + 1, j):
        solve(grid,visited,i + 1, j, dest_x, dest_y, curr_dist + 1,min_dist,shortestPath,currentPath)
    # go to right cell
    if isValid(i, j + 1) and isSafe(grid,visited,i, j + 1):
        solve(grid,visited,i, j + 1, dest_x, dest_y, curr_dist + 1,min_dist,shortestPath,currentPath)

    # go to top cell
    if isValid(i - 1, j) and isSafe(grid,visited,i - 1, j):
        solve(grid,visited,i - 1, j, dest_x, dest_y, curr_dist + 1,min_dist,shortestPath,currentPath)

    # go to left cell
    if isValid(i, j - 1) and isSafe(grid,visited,i, j - 1):
        solve(grid,visited,i, j - 1, dest_x, dest_y, curr_dist + 1,min_dist,shortestPath,currentPath)
    visited[i][j] = False
    currentPath.pop()

if __name__ == "__main__":
    import pandas as pd
    from collections import deque

    # Read data from file 'filename.csv'
    # (in the same directory that your python process is based)
    # Control delimiters, rows, column names with read_csv (see later)
    data = pd.read_csv("2d_array.csv")

    data.drop(data.columns[0], axis=1, inplace=True)
    # Preview the first 5 lines of the loaded data
    numpy_matrix = data.as_matrix()
    min_dist = [9e10] # Start from infinity
    shortestPath = [] # It will contain the path (y,x) tuples
    currentPath = [] # It will store the current path temporarily
    grid = [
        [' ', '#', ' ', '#', ' '],
        [' ', '#', ' ', '#', ' '],
        [' ', '#', ' ', '#', ' '],
        [' ', '#', ' ', '#', ' '],
        [' ', '#', ' ', '#', ' '],
        [' ', '#', ' ', '#', ' '],
        [' ', '#', ' ', '#', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ['#', ' ', '#', ' ', ' '],
        [' ', ' ', '#', '#', '#']
    ]
    print(numpy_matrix.shape)
    visited = []
    for i in range(M):
        _list = list()
        for j in range(N):
            _list.append(False)
        visited.append(_list)
    solve(numpy_matrix,visited,M-1,0,0,N-1,0,min_dist,shortestPath,currentPath)
    print("Minimum distance: ",min_dist[0])
    print("Path: [",end=" ")
    for path in shortestPath:
        print('('+str(path[0])+','+str(path[1])+')',end=' ')
    print("]")
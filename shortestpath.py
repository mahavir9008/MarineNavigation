# Load the Pandas libraries with alias 'pd'
import pandas as pd
from collections import deque
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("2d_array.csv")

data.drop(data.columns[0], axis=1, inplace=True)
# Preview the first 5 lines of the loaded data
numpy_matrix = data.as_matrix()


ROW = rows = len(numpy_matrix)
COL = columns = len(numpy_matrix[0])


# To store matrix cell cordinates
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # A data structure for queue used in BFS


class queueNode:
    def __init__(self, pt: Point, dist: int):
        self.pt = pt  # The cordinates of the cell
        self.dist = dist  # Cell's distance from the source
       # print("Transverse %s is %s" % (pt.x, pt.y))


# Check whether given cell(row,col)
# is a valid cell or not
def isValid(row: int, col: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)


# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
rowNum = [-1, 0, 0, 1,-1, 1,-1, 1]
colNum = [0, -1, 1, 0,-1, 1, 1, -1]


# Function to find the shortest path between
# a given source cell to a destination cell.
def BFS(mat, src: Point, dest: Point):
    # check source and destination cell
    # of the matrix have value 1
    if mat[src.x][src.y] != 255 or mat[dest.x][dest.y] != 255:
        return -1

    visited = [[False for i in range(COL)] for j in range(ROW)]

    # Mark the source cell as visited
    visited[src.x][src.y] = True

    # Create a queue for BFS
    q = deque()

    # Distance of source cell is 0
    s = queueNode(src, 0)
    q.append(s)  # Enqueue source cell

    # Do a BFS starting from source cell
    while q:

        curr = q.popleft()  # Dequeue the front cell

        # If we have reached the destination cell,
        # we are done
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:

            return curr.dist


            # Otherwise enqueue its adjacent cells
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            # if adjacent cell is valid, has path
            # and not visited yet, enqueue it.
            if (isValid(row, col) and mat[row][col] == 255 and not visited[row][col]):
                visited[row][col] = True
                if catch_index_error(curr.dist) is None:
                    mylist.insert(curr.dist,Point(row,col))

                Adjcell = queueNode(Point(row, col), curr.dist + 1)
                q.append(Adjcell)


                # Return -1 if destination cannot be reached
    return -1

def catch_index_error(index):
  try:
     return mylist[index]
  except IndexError:
    return None



mylist = []
source = Point(0, 1)
dest = Point(ROW-1, COL-1)
dist = BFS(numpy_matrix, source, dest)
print("Shortest Path is", len(mylist))
for x1 in range(len(mylist)):
    print("Coordinates %s is %s" % (mylist[x1].x, mylist[x1].y))

if dist != -1:
    print("Shortest Path is", dist)
else:
    print("Shortest Path doesn't exist")


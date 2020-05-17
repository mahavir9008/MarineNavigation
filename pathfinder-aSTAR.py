import heapq
import csv
import numpy as np
import pandas as pd
import collections
data = pd.read_csv("2d_array.csv")
data.drop(data.columns[0], axis=1, inplace=True)
numpy_matrix = data.to_numpy()

ROW = 202 #x
COL = 229 #y

class Node():
    #node class keeping its score,parent and position for A* Pathfinding

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

 #Heuristic used is the Manhattan distance with a tie breaker for equally scored nodes
def heuristic(xA,yA,xB,yB):
  dx = abs(xA-xB)
  dy = abs(yA-yB)
  return 1*(dx+dy)+ 1*min(dx,dy)

def astar(grid, start, end ):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)

    end_node = Node(None, end)
    start_node.g = 0  # dist btwn start node and current
    start_node.h = heuristic(start_node.position[0], start_node.position[1], end_node.position[0],
                                   end_node.position[1])  # dist btwn current and end node
    start_node.f = start_node.g + start_node.h  # total score of node < the lower the better

    end_node.g = start_node.h
    end_node.h = 0
    end_node.f = end_node.g + end_node.h
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        print(current_node.position)
        current_index = 0

        for index, item in enumerate(open_list):


            if item.f < current_node.f:
                print('item' + str(item.position))
                print(item.f)
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        print(f'in closed_list:{current_node.position}')
        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []

        for dir in dirs:  # Adjacent squares

            # Get node position

            neighbor = ((current_node.position[0] + dir[0], current_node.position[1] + dir[1]))

            # Make sure within range


            if int(neighbor[0]) > (len(grid) - 1) or int(neighbor[0]) < 0 or int(neighbor[1]) > (len(grid[len(grid) - 1]) - 1) or int(neighbor[1]) < 0:

                print(f"Position:{neighbor} out of bounds.")
                continue

                # Make sure traversable path
                # 255 is water
                # 0 is land

            if grid[neighbor[0]][neighbor[1]] != 255:
                print(f"Position:{neighbor} is land.")

                continue

            # Create new node and Append
            print(current_node.position)
            print(neighbor)
            new_node = Node(current_node, neighbor)
            children.append(new_node)
            print(f'appended to children {new_node.position}')


        # Loop through children
        for child in children:
            #print(child)
            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            
            child.g = current_node.g + 1
            h = heuristic(current_node.position[0],current_node.position[1],end_node.position[0],end_node.position[1])
            
            #tie breaker for equal scoring nodes
            p= 1.0 + (1/h) 
            child.h = h*p
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    #print(open_node)
                    continue

            # Add the child to the open list
            open_list.append(child)
            print(f'in open list  {child.position} dist:{child.g}')



def main():

    # grid = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # src = (0, 1)
    # end = (201, 228)

    src = (0, 1)
    end = (201, 228)
    grid = numpy_matrix
    path = astar(grid, src, end)
    print(path)

if __name__ == '__main__':
    main()

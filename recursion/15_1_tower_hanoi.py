'''
Flood fill algorithm: Given a 2D array, a start node, start color, and replacement color, fill all nodes in the array that are connected to the start node 
8 directional flood fill implementation
'''

class FloodFill: 

  def __init__(self, INVALID_CELL):
    self.INVALID_CELL = INVALID_CELL

  def flood_fill(self, arr, start_node: tuple, start_color, rep_color):

    if(arr[start_node[0]][start_node[1]] == self.INVALID_CELL):
      return 

    if(arr[start_node[0]][start_node[1]] == start_color):
      arr[start_node[0]][start_node[1]] = rep_color

    for i in range(start_node[0]-1, start_node[0]+2, 1):
      for j in range(start_node[1]-1, start_node[1]+2, 1): 
        # if we're not out of bounds of if we're not in an invalid cell, fill

        if 0 <= i and i < len(arr) and 0 <= j and j < len(arr[0]) and not arr[i][j] == self.INVALID_CELL \
        and not arr[i][j] == rep_color:
          arr[i][j] = rep_color
          self.flood_fill(arr, (i,j), start_color, rep_color)

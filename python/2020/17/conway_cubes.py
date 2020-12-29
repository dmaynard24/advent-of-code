class ConwayCubes:
  def __init__(self, initial):
    initial = [list(row) for row in initial.split('\n')]
    self.grid = {0: initial}

  def expand_grid(self, i):
    for z in self.grid:
      top_row = [['.'] * (len(self.grid[z][0]) + 2)]
      bottom_row = [['.'] * (len(self.grid[z][0]) + 2)]
      expanded_z = top_row + [['.'] + row + ['.'] for row in self.grid[z]] + bottom_row
      self.grid[z] = expanded_z
    # append new planes to self.grid
    self.grid[-i] = self.get_empty_plane()
    self.grid[i] = self.get_empty_plane()

  def pretty_print(self):
    for z in self.grid:
      print(z)
      print('\n'.join([''.join(val) for val in self.grid[z]]))
      print('\n')

  def get_empty_plane(self):
    row_count, col_count = len(self.grid[0]), len(self.grid[0][0])
    return [['.' for col in range(col_count)] for row in range(row_count)]

  def get_2d_adjacent_active_cube_count(self, row, col, relative_z, z):
    count = 0
    row_count, col_count = len(self.grid[0]), len(self.grid[0][0])
    if z in self.grid:
      for r in range(row - 1, row + 2):
        if r < 0 or r >= row_count:
          continue
        for c in range(col - 1, col + 2):
          if c < 0 or c >= col_count:
            continue
          if relative_z == z and (r == row and c == col):
            continue
          if self.grid[z][r][c] == '#':
            count += 1
    return count

  def get_adjacent_active_cube_count(self, row, col, z):
    below_plane_count = self.get_2d_adjacent_active_cube_count(row, col, z, z - 1)
    current_plane_count = self.get_2d_adjacent_active_cube_count(row, col, z, z)
    above_plane_count = self.get_2d_adjacent_active_cube_count(row, col, z, z + 1)
    return below_plane_count + current_plane_count + above_plane_count

  def __main__(self):
    i = 1
    while i <= 1:
      self.expand_grid(i)
      row_count, col_count = len(self.grid[0]), len(self.grid[0][0])
      new_grid = {}
      for z in range(-i, i + 1):
        new_cubes = self.get_empty_plane()
        for row in range(row_count):
          for col in range(col_count):
            count = self.get_adjacent_active_cube_count(row, col, z)
            cube_val = self.grid[z][row][col]
            # print(row, col, cube_val, count)
            if cube_val == '#':
              if count == 2 or count == 3:
                new_cubes[row][col] = '#'
            else:
              if count == 3:
                new_cubes[row][col] = '#'
        new_grid[z] = new_cubes

      self.grid = new_grid
      self.pretty_print()
      i += 1

    return self.grid


c = ConwayCubes('''.#.
..#
###''')

print(c.__main__())
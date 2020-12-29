# --- Day 17: Conway Cubes ---
# As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole contact you. They'd like some help debugging a malfunctioning experimental energy source aboard one of their super-secret imaging satellites.

# The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained in a pocket dimension! When you hear it's having problems, you can't help but agree to take a look.

# The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (x,y,z), there exists a single cube which is either active or inactive.

# In the initial state of the pocket dimension, almost all cubes start inactive. The only exception to this is a small flat region of cubes (your puzzle input); the cubes in this region start in the specified active (#) or inactive (.) state.

# The energy source then proceeds to boot up by executing six cycles.

# Each cube only ever considers its neighbors: any of the 26 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at x=0,y=2,z=3, and so on.

# During a cycle, all cubes simultaneously change their state according to the following rules:

# If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
# If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
# The engineers responsible for this experimental energy source would like you to simulate the pocket dimension and determine what the configuration of cubes should be at the end of the six-cycle boot process.

# For example, consider the following initial state:

# .#.
# ..#
# ###
# Even though the pocket dimension is 3-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1 region of the 3-dimensional space.)

# Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given z coordinate (and the frame of view follows the active cells in each cycle):

# Before any cycles:

# z=0
# .#.
# ..#
# ###

# After 1 cycle:

# z=-1
# #..
# ..#
# .#.

# z=0
# #.#
# .##
# .#.

# z=1
# #..
# ..#
# .#.

# After 2 cycles:

# z=-2
# .....
# .....
# ..#..
# .....
# .....

# z=-1
# ..#..
# .#..#
# ....#
# .#...
# .....

# z=0
# ##...
# ##...
# #....
# ....#
# .###.

# z=1
# ..#..
# .#..#
# ....#
# .#...
# .....

# z=2
# .....
# .....
# ..#..
# .....
# .....

# After 3 cycles:

# z=-2
# .......
# .......
# ..##...
# ..###..
# .......
# .......
# .......

# z=-1
# ..#....
# ...#...
# #......
# .....##
# .#...#.
# ..#.#..
# ...#...

# z=0
# ...#...
# .......
# #......
# .......
# .....##
# .##.#..
# ...#...

# z=1
# ..#....
# ...#...
# #......
# .....##
# .#...#.
# ..#.#..
# ...#...

# z=2
# .......
# .......
# ..##...
# ..###..
# .......
# .......
# .......
# After the full six-cycle boot process completes, 112 cubes are left in the active state.

# Starting with your given initial configuration, simulate six cycles. How many cubes are left in the active state after the sixth cycle?


class ConwayCubes:
  def __init__(self, initial):
    initial = [list(row) for row in initial.split('\n')]
    self.grid = {0: initial}

  def get_total_active_cube_count(self):
    count = 0
    row_count, col_count = len(self.grid[0]), len(self.grid[0][0])
    for z in self.grid:
      for row in range(row_count):
        for col in range(col_count):
          if self.grid[z][row][col] == '#':
            count += 1
    return count

  def get_empty_plane(self):
    row_count, col_count = len(self.grid[0]), len(self.grid[0][0])
    return [['.' for col in range(col_count)] for row in range(row_count)]

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

  def __main__(self, cycle_count):
    i = 1
    while i <= cycle_count:
      self.expand_grid(i)
      row_count, col_count = len(self.grid[0]), len(self.grid[0][0])
      new_grid = {}
      for z in range(-i, i + 1):
        new_plane = self.get_empty_plane()
        for row in range(row_count):
          for col in range(col_count):
            count = self.get_adjacent_active_cube_count(row, col, z)
            cube_val = self.grid[z][row][col]
            if cube_val == '#':
              if count == 2 or count == 3:
                new_plane[row][col] = '#'
            else:
              if count == 3:
                new_plane[row][col] = '#'
        new_grid[z] = new_plane
      self.grid = new_grid
      i += 1
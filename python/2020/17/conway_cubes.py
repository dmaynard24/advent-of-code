def conway_cubes(initial):
  grid = {0: initial.split('\n')}

  def get_2d_adjacent_active_cube_count(row, col, z):
    row_count = len(grid[0])
    col_count = len(grid[0][0])
    count = 0
    if z in grid:
      for r in range(row - 1, row + 2):
        if r < 0 or r >= row_count:
          continue
        for c in range(col - 1, col + 2):
          if c < 0 or c >= col_count or (r == row and c == col):
            continue
          if grid[z][r][c] == '#':
            count += 1
    return count

  def get_adjacent_active_cube_count(row, col, z):
    below_plane_count = get_2d_adjacent_active_cube_count(row, col, z - 1)
    current_plane_count = get_2d_adjacent_active_cube_count(row, col, z)
    above_plane_count = get_2d_adjacent_active_cube_count(row, col, z + 1)
    return below_plane_count + current_plane_count + above_plane_count

  i = 0
  while i < 3:
    row_count = len(grid[0])
    col_count = len(grid[0][0])
    for z in grid:
      new_cubes = [[None for col in range(col_count)] for row in range(row_count)]
      for row in range(row_count):
        for col in range(col_count):
          count = get_adjacent_active_cube_count(row, col, z)
          cube_val = grid[z][row][col]

  return grid


print(conway_cubes('''.#.
..#
###'''))
# --- Day 12: Rain Risk ---
# Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!

# Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

# The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. After staring at them for a few minutes, you work out what they probably mean:

# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship is currently facing.
# The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

# For example:

# F10
# N3
# F7
# R90
# F11
# These instructions would be handled as follows:

# F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
# N3 would move the ship 3 units north to east 10, north 3.
# F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
# R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
# F11 would move the ship 11 units south to east 17, south 8.
# At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.

# Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?

COMPASS_DIRECTIONS = ['N', 'E', 'S', 'W']


def move(x, y, compass_direction, distance):
  if compass_direction == 'N':
    y += distance
  elif compass_direction == 'S':
    y -= distance
  elif compass_direction == 'E':
    x += distance
  elif compass_direction == 'W':
    x -= distance
  return x, y


def rain_risk(instructions):
  instructions = instructions.split('\n')

  x = 0
  y = 0
  direction_index = 1
  for ins in instructions:
    action = ins[0]
    value = int(ins[1:])
    if action == 'N' or action == 'E' or action == 'S' or action == 'W':
      x, y = move(x, y, action, value)
    elif action == 'L':
      direction_index = (direction_index - value // 90) % len(COMPASS_DIRECTIONS)
    elif action == 'R':
      direction_index = (direction_index + value // 90) % len(COMPASS_DIRECTIONS)
    elif action == 'F':
      x, y = move(x, y, COMPASS_DIRECTIONS[direction_index], value)

  return abs(x) + abs(y)


# TODO: part 2


def rain_risk_part_2(instructions):
  instructions = instructions.split('\n')

  def rotate_waypoint(x, y, quadrant_index):
    return [(x, y), (-y, x), (-x, -y), (y, -x)][quadrant_index]

  def get_quadrant_index_from_coords(x, y, quadrant_index):
    if x > 0 and y > 0:
      return 0
    elif x < 0 and y > 0:
      return 1
    elif x < 0 and y < 0:
      return 2
    elif x > 0 and y < 0:
      return 3
    return quadrant_index

  x = 0
  y = 0
  waypoint_x = 10
  waypoint_y = 1
  quadrant_index = 0
  for ins in instructions:
    action = ins[0]
    value = int(ins[1:])
    if action == 'N' or action == 'E' or action == 'S' or action == 'W':
      waypoint_x, waypoint_y = move(waypoint_x, waypoint_y, action, value)
      quadrant_index = get_quadrant_index_from_coords(waypoint_x, waypoint_y, quadrant_index)
    elif action == 'L':
      quadrant_index = (quadrant_index + value // 90) % len(COMPASS_DIRECTIONS)
      waypoint_x, waypoint_y = rotate_waypoint(waypoint_x, waypoint_y, quadrant_index)
    elif action == 'R':
      quadrant_index = (quadrant_index - value // 90) % len(COMPASS_DIRECTIONS)
      waypoint_x, waypoint_y = rotate_waypoint(waypoint_x, waypoint_y, quadrant_index)
    elif action == 'F':
      x += (waypoint_x * value)
      y += (waypoint_y * value)

  return abs(x) + abs(y)


print(rain_risk_part_2('''F10
N3
F7
R90
F11'''))
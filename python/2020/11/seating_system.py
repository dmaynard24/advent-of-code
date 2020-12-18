# --- Day 11: Seating System ---
# Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

# By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

# The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

# L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
# Floor (.) never changes; seats don't move, and nobody sits on the floor.

# After one round of these rules, every seat in the example layout becomes occupied:

# #.##.##.##
# #######.##
# #.#.#..#..
# ####.##.##
# #.##.##.##
# #.#####.##
# ..#.#.....
# ##########
# #.######.#
# #.#####.##
# After a second round, the seats with four or more occupied adjacent seats become empty again:

# #.LL.L#.##
# #LLLLLL.L#
# L.L.L..L..
# #LLL.LL.L#
# #.LL.LL.LL
# #.LLLL#.##
# ..L.L.....
# #LLLLLLLL#
# #.LLLLLL.L
# #.#LLLL.##
# This process continues for three more rounds:

# #.##.L#.##
# #L###LL.L#
# L.#.#..#..
# #L##.##.L#
# #.##.LL.LL
# #.###L#.##
# ..#.#.....
# #L######L#
# #.LL###L.L
# #.#L###.##
# #.#L.L#.##
# #LLL#LL.L#
# L.L.L..#..
# #LLL.##.L#
# #.LL.LL.LL
# #.LL#L#.##
# ..L.L.....
# #L#LLLL#L#
# #.LLLLLL.L
# #.#L#L#.##
# #.#L.L#.##
# #LLL#LL.L#
# L.#.L..#..
# #L##.##.L#
# #.#L.LL.LL
# #.#L#L#.##
# ..L.L.....
# #L#L##L#L#
# #.LLLLLL.L
# #.#L#L#.##
# At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

# Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?


def seating_system(seats):
  seats = seats.split('\n')

  def get_adjacent_occupied_seat_count(row, col):
    count = 0
    for r in range(row - 1, row + 2):
      if r < 0 or r >= len(seats):
        continue
      for c in range(col - 1, col + 2):
        if c < 0 or c >= len(seats[0]) or (r == row and c == col):
          continue
        if seats[r][c] == '#':
          count += 1
    return count

  total_occupied_count = 0
  did_change = True
  while did_change:
    did_change = False
    new_seats = [[None for col in range(len(seats[0]))] for row in range(len(seats))]
    total_occupied_count = 0

    for row in range(len(seats)):
      for col in range(len(seats[0])):
        count = get_adjacent_occupied_seat_count(row, col)
        seat_val = seats[row][col]
        if seat_val == 'L' and count == 0:
          new_seats[row][col] = '#'
          total_occupied_count += 1
          did_change = True
        elif seat_val == '#' and count >= 4:
          new_seats[row][col] = 'L'
          did_change = True
        else:
          # no change
          if seat_val == '#':
            total_occupied_count += 1
          new_seats[row][col] = seat_val

    seats = new_seats

  return total_occupied_count

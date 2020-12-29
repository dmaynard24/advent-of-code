import unittest, conway_cubes


class TestConwayCubes(unittest.TestCase):
  def test_conway_cubes(self):
    c = conway_cubes.ConwayCubes('''.#.
..#
###''')
    c.__main__(6)
    self.assertEqual(c.get_total_active_cube_count(), 112)

  def test_conway_cubes_1(self):
    c = conway_cubes.ConwayCubes('''..#..#..
.###..#.
#..##.#.
#.#.#.#.
.#..###.
.....#..
#...####
##....#.''')
    c.__main__(6)
    self.assertEqual(c.get_total_active_cube_count(), 242)


if __name__ == '__main__':
  unittest.main()
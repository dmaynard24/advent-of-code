import unittest, shuttle_search


class TestShuttleSearch(unittest.TestCase):
  def test_shuttle_search(self):
    self.assertEqual(shuttle_search.shuttle_search('''939
7,13,x,x,59,x,31,19'''), 295)

  def test_shuttle_search_1(self):
    self.assertEqual(
        shuttle_search.shuttle_search('''1000067
17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,439,x,29,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,787,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,19'''
                                      ), 205)

  def test_shuttle_search_part_2(self):
    self.assertEqual(shuttle_search.shuttle_search_part_2('7,13,x,x,59,x,31,19'), 1_068_781)

  def test_shuttle_search_part_2_1(self):
    self.assertEqual(shuttle_search.shuttle_search_part_2('17,x,13,19'), 3_417)

  def test_shuttle_search_part_2_2(self):
    self.assertEqual(shuttle_search.shuttle_search_part_2('67,7,59,61'), 754_018)

  def test_shuttle_search_part_2_3(self):
    self.assertEqual(shuttle_search.shuttle_search_part_2('67,x,7,59,61'), 779_210)

  def test_shuttle_search_part_2_4(self):
    self.assertEqual(shuttle_search.shuttle_search_part_2('67,7,x,59,61'), 1_261_476)

  def test_shuttle_search_part_2_5(self):
    self.assertEqual(shuttle_search.shuttle_search_part_2('1789,37,47,1889'), 1_202_161_486)

  # def test_shuttle_search_part_2_6(self):
  #   self.assertEqual(
  #       shuttle_search.shuttle_search_part_2(
  #           '17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,439,x,29,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,787,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,19'
  #       ), 1_202_161_486)


if __name__ == '__main__':
  unittest.main()
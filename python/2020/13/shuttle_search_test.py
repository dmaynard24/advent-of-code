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


if __name__ == '__main__':
  unittest.main()
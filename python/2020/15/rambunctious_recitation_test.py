import unittest, rambunctious_recitation


class TestRambunctiousRecitation(unittest.TestCase):
  def test_rambunctious_recitation(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('0,3,6'), 436)

  def test_rambunctious_recitation_1(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('1,3,2'), 1)

  def test_rambunctious_recitation_2(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('2,1,3'), 10)

  def test_rambunctious_recitation_3(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('1,2,3'), 27)

  def test_rambunctious_recitation_4(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('2,3,1'), 78)

  def test_rambunctious_recitation_5(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('3,2,1'), 438)

  def test_rambunctious_recitation_6(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('3,1,2'), 1_836)

  def test_rambunctious_recitation_7(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('1,12,0,20,8,16'), 273)


if __name__ == '__main__':
  unittest.main()
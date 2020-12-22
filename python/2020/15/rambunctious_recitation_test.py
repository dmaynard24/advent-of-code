import unittest, rambunctious_recitation


class TestRambunctiousRecitation(unittest.TestCase):
  def test_rambunctious_recitation(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('0,3,6', 2020), 436)

  def test_rambunctious_recitation_1(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('1,3,2', 2020), 1)

  def test_rambunctious_recitation_2(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('2,1,3', 2020), 10)

  def test_rambunctious_recitation_3(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('1,2,3', 2020), 27)

  def test_rambunctious_recitation_4(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('2,3,1', 2020), 78)

  def test_rambunctious_recitation_5(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('3,2,1', 2020), 438)

  def test_rambunctious_recitation_6(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('3,1,2', 2020), 1_836)

  def test_rambunctious_recitation_7(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('1,12,0,20,8,16', 2020), 273)

  def test_rambunctious_recitation_8(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('0,3,6', 30_000_000), 175_594)

  def test_rambunctious_recitation_9(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('1,3,2', 30_000_000), 2_578)

  def test_rambunctious_recitation_10(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('2,1,3', 30_000_000), 3_544_142)

  def test_rambunctious_recitation_11(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('1,2,3', 30_000_000), 261_214)

  def test_rambunctious_recitation_12(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('2,3,1', 30_000_000), 6_895_259)

  def test_rambunctious_recitation_13(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('3,2,1', 30_000_000), 18)

  def test_rambunctious_recitation_14(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('3,1,2', 30_000_000), 362)

  def test_rambunctious_recitation_15(self):
    self.assertEqual(rambunctious_recitation.rambunctious_recitation('1,12,0,20,8,16', 30_000_000), 47_205)


if __name__ == '__main__':
  unittest.main()
import unittest
import json
from stag import func_sorted
from stag import func1

with open('data_db.json') as f_obj:
	data = json.load(f_obj)

main_lst = data["main_lst"]
data = data["data"]
class TestUM(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

#	def test_1(self):
#		self.assertEqual(func1(a,b), 2)

	def test(self):
		for i in range(10):
			self.assertEqual(func1(main_lst,data[i][0]),data[i][-1])

	def test_sorted(self):
		for i in range(10):
			self.assertEqual(func_sorted(main_lst,data[i][0]),data[i][-1])

	def test_equal(self):
		for i in range(len(data)):
			self.assertEqual(func1(main_lst,data[i][0]),func_sorted(main_lst, data[i][0]))

if __name__ == '__main__':
	unittest.main()
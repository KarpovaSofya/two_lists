import unittest
import json
from stag import func_sorted
from stag import func1
from stag import func_bad

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
		for i in range(len(data)):
			self.assertEqual(func1(main_lst,data[i][0]),data[i][-1])

	def test_sorted(self):
		for i in range(len(data)):
			self.assertEqual(func_sorted(main_lst,data[i][0]),data[i][-1])
# test и test_sorted в качестве второго аргумента принимает уже посчитанное с помощью функции func_bad значение для того, чтобы сократить время тестирования.
# Можно использовать тест, где сравнение будет происходить с результатом функции func_bad (значение высчитывается прямо в теле теста).

	def test_main(self):
		for i in range(len(data)):
			self.assertEqual(func_sorted(main_lst,data[i][0]),func_bad(main_lst,data[i][0]))

	def test_equal(self):
		for i in range(len(data)):
			self.assertEqual(func1(main_lst,data[i][0]),func_sorted(main_lst, data[i][0]))

	def test_reverse1(self):
		for i in range(len(data)):
			self.assertEqual(func1(main_lst,data[i][0]),func1(data[i][0],main_lst))

	def test_reverse2(self):
		for i in range(len(data)):
			self.assertEqual(func_sorted(data[i][0],main_lst),func_sorted(main_lst, data[i][0]))

if __name__ == '__main__':
	unittest.main()
import random
import time
import json
import matplotlib.pyplot as plt

with open('data_db.json') as f_obj:
	data = json.load(f_obj)

# генерация списка длины l, из неповторяющихся случайных величин
def generate_list(l):
	#l = random.randint(1,20)
	lst = set()
	while len(lst) < l:
		lst.add(random.randint(-10000,10000))
	return(list(lst))

# список с неповторяющимися элементами, длина которого не превосходит l; работает быстрее, но нельзя заранее задать длину списка
def generate_list_faster(l):
	lst = set(random.randint(-10000,10000) for x in range(0,l))
	return(list(lst))

#основная функция; недостаток - так можно только в Python
def func1(a,b):
	c = a + b
	num = len(c) - len(set(c))
	return(num)

# func_bad работает очень медленно, но гарантированно правильно. Использую её для проверки правильности
def func_bad(a,b):
	k = 0
	if len(a) < len(b):
		for i in a:
			if i in b:
				k += 1
	else:
		for i in b:
			if i in a:
				k += 1
	return k

# ещё один вариант реализации
def func_sorted(a,b):
	a = sorted(a)
	b = sorted(b)
	min_el_index = 0
	max_el_index = -1
	i = 0
	k = 0

	if len(a) < len(b):
		(a,b) = (b,a)
	max_el = b[-1]
	min_el = b[0]
	while a[i] <= max_el:
		if a[i] < min_el:
			min_el_index = i+1

		if a[i] <= max_el:
			max_el_index = i+1

		i += 1
		if i == len(a) - 1:
			break

	if max_el_index == len(a):
		a = a[min_el_index:]
	else:
		a = a[min_el_index: max_el_index]
	for i in b:
		if i in a:
			k += 1
	return k
# Создание данных

def generate_data():
	main_lst = generate_list(1000) # список, с которым будут проходить все сравнения
	for i in range(10):
		l = generate_list(1000)
		data_list.append([l, func_bad(main_lst,l)]) # data_list - используется в тестах, чтобы каждый раз не тратить время на долгую func_bad
	
	list_for_times = [generate_list(i) for i in range(10000,100001, 1000)] # для сравнения времени работы функций

	time_list_bad = []
	time_list = []
	time_list_sorted =[]

	for i in list_for_times:
		t0 = time.time()
		func1(main_lst,i)
		time_list.append(time.time() - t0)

		t0 = time.time()
		func_bad(main_lst,i)
		time_list_bad.append(time.time() - t0)

		t0 = time.time()
		func_sorted(main_lst,i)
		time_list_sorted.append(time.time() - t0)

	data = {"data":data_list, "main_lst": main_lst, "time_list": time_list, "time_list_bad": time_list_bad, "time_list_sorted": time_list_sorted}

	with open('data_db.json','w') as outfile:
		json.dump(data,outfile)

#построение графиков времени работы функций
def time_plot():
	fig = plt.figure()

	plt.plot(list(range(10000,100001, 1000)), data["time_list"], label='time_func')
	plt.plot(list(range(10000,100001, 1000)), data["time_list_bad"], label='time_func_bad')
	plt.plot(list(range(10000,100001, 1000)), data["time_list_sorted"], label='time_func_sorted')

	plt.legend()
	plt.show()

time_plot()

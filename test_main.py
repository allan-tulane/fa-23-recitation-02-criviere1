from main import *

def test_simple_work():
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(8, 4, 2) == 120
	assert simple_work_calc(9, 3, 3) == 27
	assert simple_work_calc(20, 4, 5) == 52

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(8, 4, 2, lambda n: n+1) == 141
	assert work_calc(9, 3, 3, lambda n: n//2) == 16
	assert work_calc(20, 5, 4, lambda n: 3*n) == 160
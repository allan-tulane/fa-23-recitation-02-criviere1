### the only imports needed are here

import tabulate
import time
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
	print(n)
	if (n == 1):
		return 1
	else:
		new_n = n//b
		return (a * simple_work_calc(new_n, a, b) + n)
	pass

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if (n == 1):
		return 1
	else:
		new_n = n//b
		F = f(n)
		print(n)
		print(F)
		return (a * work_calc(new_n, a, b, f) + F)
	pass

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if (n == 1):
		return n
	else:
		new_n = n//b
		F = f(n)
		print(n)
		print(F)
		return (a * span_calc(new_n, a, b, f) + F)
	pass

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))
def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for
	given input sizes.
	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			span_fn1(n),
			span_fn2(n)
			))
	return result
				
def test_compare_work():
	# curry work_calc to create multiple work
	# functions that can be passed to compare_work
	work_fn1[1] = 1
	work_fn2[1] = 1

	# create work_fn1
	work_fn1 = lambda n:2*work_fn1(n//2)+work_fn1(n)
	# create work_fn2
	work_fn2 = lambda n:2*work_fn2(n//2)+work_fn2(n*n)

	res = compare_work(work_fn1, work_fn2)
	print(res)

def test_compare_span():
	# TODO
	assert span_calc(10,2,2, lambda n:1) == 15
	assert span_calc(20,1,4, lambda n:n*n) == 426
	assert span_calc(30,3,4, lambda n:n) == 60
# What does each of foo_x do?

def foo_1(x):
	return x ** 0.5

# a function to find the square root of X

def foo_2(x, y):
	if x > y:
		return x
	return y

# if X is more than Y then return x and y

def foo_3(x, y, z):
	if x > y:
		tmp = y
		y = x
		x = tmp
	if y > z:
		tmp = z
		z = y
		y = tmp
	return [x, y, z]

# if x is more than y then swap around X and Y variables. If y is more than Z then swap around Y and Z variables.

def foo_4(x):
	result = 1
	for i in range(1, x + 1):
		result = result * i
	return result

# Returning the final iteration of the loop with result = result * i

def foo_5(x): # a recursive function that calculates the factorial of x
	if x == 1:
		return 1
	return x * foo5(x - 1)

def foo_6(x): # Calculate the factorial of x in a different way
	facto = 1
	while x >= 1:
		facto = facto * x
		x = x - 1
	return facto






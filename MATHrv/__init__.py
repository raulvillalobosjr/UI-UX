def addition(a, b):
	return a+b

def add1(num):
	return num+1

def tri_area(base, height):
	return (base*height)/2

def next_edge(side1, side2):
	return (side1 + side2)-1

def remainder(x, y):
	return x%y

def string_int(txt):
	return int(txt)

def find_perimeter(length, width):
	return (length+width)*2

def sum_polygon(n):
	return (n-2)*180

def calculate_exponent(num, exp):
	return num**exp

def squared(b):
	return b*b

def to_int(txt):
	return int(txt)

def to_str(num):
	return str(num)

def is_seven(x):
	return x==7

def swap(a, b):
	b1 = a
	a1 = b
	return [a1, b1]

def is_same_num(num1, num2):
	return num1 == num2

def less_than_or_equal_to_zero(num):
	return num<=0

def mod(m, n):
	return m%n

def even_or_odd(lst):
	if sum(lst)%2==0:
		return "even"
	else:
		return "odd"

def findLargestNum(nums):
	return sorted(nums)[-1]

def find_smallest_num(lst):
	return sorted(lst)[0]

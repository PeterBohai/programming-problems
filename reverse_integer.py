""" Solution 1 (Pythonic)

	1) Convert the integer into a string
	2) Reverse the string
	3) Convert the reversed String back into an integer
	4) Return the result

	Time: O(N), O(log(X)) --> N is the number of digits in X
	Space: O(N)

	drawbacks: 
	 - extra O(N) operations (converting a string to and from integer all take linear time)
"""
def reverse_pythonic(self, x: int) -> int:
	MAX_INT = 2 ** 31 - 1
	MIN_INT = -2 ** 31
	
	sign = 1 if x > 0 else -1
	num_str = str(abs(x))
	reversed_num = int(num_str[::-1]) * sign
	if MIN_INT <= reversed_num <= MAX_INT:
		return reversed_num
	return 0

""" Solution 2 (Standard)

	1) Extract the right-most digit of x (modulus operator)
	2) Get rid of the extracted digit and update x (integer division)
	3) Push the digit onto the result
	4) Return the result when x becomes 0

	Time: O(N), O(log(X)) --> N is the number of digits in X
	Space: O(1)

	drawbacks: 
	 - does not address range constraint in the most accurate sense
"""
def reverse_simple(self, x: int) -> int:
	MAX_INT = 2 ** 31 - 1
	MIN_INT = -2 ** 31
	
	sign = 1 if x > 0 else -1
	num = abs(x)				
	res = 0

	# reverse the integer, one digit at a time
	while num > 0:				
		digit = num % 10
		num //= 10
		res = res * 10 + digit
	
	res *= sign
	if MIN_INT <= res <= MAX_INT:
		return res
	return 0


""" Solution 3 (Standard + Better Conditional Checks)

	1) Extract the right-most digit of x (modulus operator)
	2) Get rid of the extracted digit and update x (integer division)
	3) Check if pushing the digit will result in an overflow
	4) Push the digit onto the result
	5) Return the result when x becomes 0

	Time: O(N), O(log(X)) --> N is the number of digits in X
	Space: O(1)
"""
def reverse_very_advanced(self, x: int) -> int:
	MAX_INT = 2 ** 31 - 1		# 2147483647
	MIN_INT = -2 ** 31			# -2147483648
	LAST_MAX_INT_DIGIT = MAX_INT % 10	# 7
	LAST_MIN_INT_DIGIT = MIN_INT % -10	# -8
	
	res = 0

	# reverse the integer, one digit at a time
	while x != 0:
		digit = x % (10 if x > 0 else -10)
		x = int(x / 10)

		# Check if appending digit to result will overflow the constraints
		if res > int(MAX_INT / 10) or (res == int(MAX_INT / 10) and digit > LAST_MAX_INT_DIGIT):
			return 0
		if res < int(MIN_INT / 10) or (res == int(MIN_INT / 10) and digit < LAST_MIN_INT_DIGIT):
			return 0

		# Append digit to previous result
		res = res * 10 + digit

	return res

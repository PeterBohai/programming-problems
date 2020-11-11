# Video Explanation: https://youtu.be/i0WwsQYrMAM

""" Solution 1 (Sorting)

	1) Sort the list (ascending order)
	2) Iterate through the sorted list
		3) Use the index as the expected number and compare to the current number
		4) If there is a mismatch, the index will be the missing number
	4) If every index matches up with the number, return N

	Time: O(NlogN)
	Space: O(1) if sorting in-place, otherwise O(N)
	
	key drawbacks: 
	 - modifying original list
	 - if we don't modify original list, we need to use O(N) extra space
	 - O(NlogN) is not the optimal time complexity
"""
def missingNumber(nums: List[int]) -> int:
	n = len(nums)						# Example: [3, 0, 1]    [1, 0, 2]
	nums.sort()                         # answer   --> 2        --> 3 == n
										
	for i, num in enumerate(nums):		# index    0  1 *2*     0  1  2  *3*
		if num != i:					# list    [0, 1, 3]    [0, 1, 2]
			return i
	return n


""" Solution 2 (Set)

	1) Create a set containing all values of the input list
	2) Iterate through the expected numbers from 0 to N
		3) If an expected number is not in the set, Return

	Time: O(N)
	Space: O(N)

	key drawback: 
	 - uses O(N) extra space
"""
def missingNumber(nums: List[int]) -> int:
	n = len(nums)
								# Example: [3, 0, 1] --> 2
	nums_set = set(nums)		# set: {3, 0, 1}
	for num in range(n + 1):    # expected nums: 0, 1, 2, 3
		if num not in nums_set:
			return num


# ** BEST SOLUTION **
""" Solution 3 (Math)

	1) Compute the sum we expect if there is no number missing (0 + 1 + ... + N)
	2) Compute the actual sum of the given input
	3) Return the difference between the expected sum and the actual sum

	Example:
		expected numbers: [a, b, c] --> a + b + c
		input: [a, c] --> a + c
		missing number: (a + b + c) - (a + c) 
						= a + b + c - a - c 
						= b
	Time: O(N)
	Space: O(1)
"""
def missingNumber(nums: List[int]) -> int:
	n = len(nums)

	# Guass' method/formula				# Example: [3, 0, 1] --> missing 2
	expected_sum = n * (n + 1) // 2     # expected: 0 + 1 + 2 + 3 = 3(3+1)/2 = 6
	actual_sum = sum(nums)				# actual: 3 + 0 + 1 = 4
	return expected_sum - actual_sum	# 6 - 4 = 2

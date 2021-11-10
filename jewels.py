

def max_jewels(nums):
	dp = [0] * len(nums)
	dp[0] = nums[0]
	dp[1] = max(nums[0], nums[1])

	for i in range(2,len(nums)):

		#We take the jewel at i
			#Total value = nums[i] + dp[i-2]

		#We dont take the jewel i
			#Total value = dp[i-1]
		dp[i] = max( nums[i] + dp[i-2] , dp[i-1] )

	return dp[len(nums) - 1]

def main(nums):
	#Base cases
	if  len(nums) == 0:
		return 0
	if len(nums) == 1:
		return nums[0]
	if len(nums) == 2:
		return max(nums)

	#Max jewel function uses dp to fine the maximum jewels in list (not in circular pattern)

	#Dont cosider the first jewel
	max_jewels_a = max_jewels(nums[1:])

	#Done consider the last jewel
	max_jewels_b = max_jewels(nums[:-1])

	return max(max_jewels_a, max_jewels_b)


import sys

if __name__ == '__main__' :
	
	lists = []

	for line in sys.stdin:

		lists.append([int(_) for _ in line.split()])
	

	for l in lists:

		daughter_1 = 0
		daughter_2 = 0

		total_jewels = sum(l)
		daughter_1 = main(l)
		daughter_2 = total_jewels - daughter_1

		print(daughter_1, daughter_2)


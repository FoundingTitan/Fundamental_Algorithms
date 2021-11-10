

import sys

def max_overlap_intervals(l):


	#Convert list elements into intervals
	interval_list = []
	for i in range(0, len(l), 2):

		interval_list.append([l[i],l[i+1]])

	#Sort based on end value
	interval_list.sort(key = lambda x: x[0])

	start_value = interval_list[0][0]
	end_value = interval_list[0][1]

	max_len = 0

	for i in range(1, len(interval_list)):
		cur_start_value = interval_list[i][0]
		cur_end_value = interval_list[i][1]

		if cur_start_value <= end_value:
			start_value = min(start_value, cur_start_value)
			end_value = max(end_value, cur_end_value)
		else:
			max_len = max (max_len, end_value - start_value)
			start_value = cur_start_value
			end_value = cur_end_value

	#print(end_value - start_value)
	max_len = max (max_len, end_value - start_value)
	print(max_len)


if __name__ == '__main__' :

	lists = []

	n = int(input())
	for i in range(0,n):
	    lists.append([int(_) for _ in input().split()])

	for l in lists:
	    max_overlap_intervals(l)
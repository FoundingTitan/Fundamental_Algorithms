
import sys

# Python3 program that print maximum
# number of overlap
# among given ranges
 
# Function that prmaximum
# overlap among ranges
def overlap(v):
    
    # print("Given list",l)

    #Convert list elements into intervals
    interval_list = []
    for i in range(0, len(v), 2):
        interval_list.append([v[i],v[i+1]])
    # print("Interval list", interval_list)

    #Sort based on end value
    interval_list.sort(key = lambda x: x[0])
    # variable to store the maximum
    # count
    ans = 0
    count = 0
    data = []
 
    # storing the x and y
    # coordinates in data vector
    for i in range(len(interval_list)):
 
        # pushing the x coordinate
        data.append([interval_list[i][0], 'x'])
 
        # pushing the y coordinate
        data.append([interval_list[i][1], 'y'])
 
    # sorting of ranges
    data = sorted(data)
    
    # Traverse the data vector to
    # count number of overlaps
    for i in range(len(data)):
 
        # if x occur it means a new range
        # is added so we increase count
        if (data[i][1] == 'x'):
            count += 1
 
        # if y occur it means a range
        # is ended so we decrease count
        if (data[i][1] == 'y'):
            count -= 1
 
        # updating the value of ans
        # after every traversal
        ans = max(ans, count)
 
    # printing the maximum value
    print(ans)
 
 

if __name__ == '__main__' :

    lists = []

    n = int(input())
    for i in range(0,n):
        lists.append([int(_) for _ in input().split()])

    for l in lists:
        overlap(l)
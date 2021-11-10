#!/usr/bin/env python
# coding: utf-8

import sys

def max_nonoverlap_intervals(l):

    # print("Given list",l)

    #Convert list elements into intervals
    interval_list = []
    for i in range(0, len(l), 2):
        interval_list.append([l[i],l[i+1]])
    # print("Interval list", interval_list)

    #Sort based on end value
    interval_list.sort(key = lambda x: x[1])
    # print("Sorted interval list", interval_list)

    num_non_overlap_intervals = 1
    end_value = interval_list[0][1]

    for i in range(1, len(interval_list)):
        cur_start_value = interval_list[i][0]
        if cur_start_value > end_value:
            num_non_overlap_intervals += 1
            end_value = interval_list[i][1]

    print(num_non_overlap_intervals)

if __name__ == '__main__' :
    
    lists = []

    n = int(input())
    for i in range(0,n):
        lists.append([int(_) for _ in input().split()])

    for l in lists:
        max_nonoverlap_intervals(l)




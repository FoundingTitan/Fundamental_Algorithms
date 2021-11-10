def pivotedBinarySearch(arr, n, target, largest):

    # print("arr",arr, "target",target)
    pivot = findPivot(arr, 0, n-1)
    # print("pivot", pivot)

    if pivot == -1:
        return binarySearch(arr, 0, n-1, target, largest)

    elif arr[pivot] == target:
        return pivot

    elif arr[0] == target:
        # print("n",n)
        first_part_ans = binarySearch(arr, 0, pivot, target, largest)
        second_part_ans = binarySearch(arr, pivot+1, n-1, target, largest)
        # print("Second part variables", pivot+1, n-1, target, largest)
        # print("first_part_ans",first_part_ans)
        # print("second_part_ans",second_part_ans)
        return max(first_part_ans, second_part_ans)

    elif arr[0] < target:
        return binarySearch(arr, 0, pivot, target, largest)

    else:
        return binarySearch(arr, pivot+1, n-1, target, largest)




def findPivot(arr, left, right):

    if right < left:
        return -1

    if left == right:
        return right

    mid = (left + right)//2

    if mid < right and arr[mid] > arr[mid+1]:
        return mid

    elif mid > left and arr[mid] < arr[mid-1]:
        return mid-1

    elif arr[left] >= arr[mid]:
        return findPivot(arr, left, mid-1)

    else:
        return findPivot(arr, mid+1, right)



def binarySearch(arr, left, right, target, largest):

    if right >= left:

        mid = (left+right)//2

        if target == arr[mid]:

            largest = mid
            return binarySearch(arr, mid+1, right, target, largest)

        elif target > arr[mid]:
            return binarySearch(arr, mid+1, right, target, largest)

        else:
            return binarySearch(arr, left, mid-1, target, largest)


    elif largest != None:
        return largest

    else:
        return -1



if __name__ == '__main__' :

#    start = timer()

    lists = []

    for i in range(0,2):
        lists.append([int(_) for _ in input().split()])

    for target in lists[1]:
        largest = None
        index = pivotedBinarySearch(lists[0], len(lists[0]), target, largest)
        print(index)




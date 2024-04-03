from typing import List
numbers = [2,8,5,3,9,4,1,7]

def mergeSort(arr, start, end, side):
    if start < end:
        # print(f'{side}({start}-{end}): {arr[start:end]}')
        mid = (start+end)//2
        mergeSort(arr, start, mid, "Left")
        mergeSort(arr, mid+1, end, "right")
        merge(arr, start, end, mid)

def merge(arr, start, end, mid):
    print("########## Merging and sorting ###########")
    print(f'Arr before: {arr}')
    temp = [0]*(end-start+1)
    print(temp)
    k = 0
    i = start
    j = mid+1

    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i+=1
            k+=1
        else:
            temp[k] = arr[j]
            j+=1
            k+=1

    while i <= mid:
        temp[k] = arr[i]
        i+=1
        k+=1

    while j <= end:
        temp[k] = arr[j]
        j+=1
        k+=1

    k = 0
    for i in range(start, end+1):
        arr[i] = temp[k]
        k+=1

    print(temp)
    print(f'Arr being sorted: {arr}') 

    


mergeSort(numbers, 0, len(numbers)-1, "All")
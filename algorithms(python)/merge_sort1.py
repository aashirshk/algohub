from typing import List

numbers = [2,8,5,3,9,4,1,7]

def mergeSort(arr: List, start, end, side):
    if start < end:
        print(f'{side}({start}-{end}): {arr[start:end]}')
        mid = (start+end)//2
        mergeSort(arr, start, mid, "Left")
        mergeSort(arr, mid+1, end, "Right")


mergeSort(numbers, 0, len(numbers), "All")
from re import L
from xml.etree.ElementTree import PI


numbers = [10, 5, 13, 8, 2]

def partition(arr, start, end):
        pivot = end

        pIndex = start

        for i in range(start, end):
            if arr[i] < arr[pivot]:
                if i != pIndex:
                    arr[i], arr[pIndex] = arr[pIndex], arr[i]
                pIndex += 1 
        
        arr[pIndex], arr[pivot] = arr[pivot], arr[pIndex]

        return pIndex

def quickSort(arr, start, end):
    if start < end:
        pIndex = partition(arr, start, end)
        quickSort(arr, start, pIndex-1)
        quickSort(arr, pIndex+1, end)


quickSort(numbers, 0, len(numbers)-1)

print(numbers)


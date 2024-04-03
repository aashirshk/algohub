from typing import List

def insertionSort(numbers: List):
    for i in range(1, len(numbers)):
        while(i>0):
            if numbers[i] < numbers[i-1]:
                numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
            i-=1


def insertionSortReverse(numbers: List):
    for i in range(1, len(numbers)):
        while(i>0):
            if numbers[i] > numbers[i-1]:
                numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
            i-=1
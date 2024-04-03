from typing import List

def bubbleSort(numbers: List):
    for i in range(0, len(numbers)-1):
        for j in range(0, len(numbers)-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    

from typing import List

def binary_search_(arr: List, element, to_right = False):
    if element == arr[0]:
        return 0
    if element == arr[-1]:
        return len(arr)-1
    if element < arr[0]:
        return 0 if to_right else -1
    if element > arr[-1]:
        return len(arr) if to_right else len(arr)-1
    
    low = 0
    high = len(arr)-1

    while high - low > 1:
        center = low + (high-low)//2
        if arr[center] > element:
            high = center
        elif arr[center] < element:
            low = center
        else:
            low = center
            break
    if to_right:
        if arr[low] < element:
            return low + 1
        else:
            return low
    return low

def binary_search(arr: List, element, to_right=False):
    low, high = -1, len(arr)
    while high - low > 1:
        mid = (low + high) // 2
        if arr[mid] > element:
            high = mid
        else:
            low = mid
    if to_right and (low == -1 or arr[low] < element):
        return low + 1
    return low

to_right = input().strip() == "r"

arr = [int(x) for x in input().strip().split(" ")]

elements = []
element = 0
while True:
    try:
        element = int(input().strip())
    except EOFError:
        break
    elements.append(element)

for e in elements:
    i = binary_search(arr, e, to_right)
    print(i)
import random
from typing import List
import timeit
import matplotlib.pyplot as plt
import sys 
sys.setrecursionlimit(20000)

def linear_search(arr: List[int], target: int) -> int:
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

def binary_search(arr: List[int], target: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000, 20000000, 50000000]
linear_times = []
binary_times = []

for size in sizes:
    arr = list(range(size, 0, -1))
    target = random.randint(0, size)
    start = timeit.default_timer()
    linear_search(arr, target)
    end = timeit.default_timer()
    linear_times.append(end - start)
    start = timeit.default_timer()
    sorted_arr = quicksort(arr)
    binary_search(sorted_arr, target)
    end = timeit.default_timer()
    binary_times.append(end - start)

print("Size\tLinear\tBinary")
for size, linear, binary in zip(sizes, linear_times, binary_times):
    print(f"{size}\t{linear}\t{binary}")

plt.figure(figsize=(10, 6))
plt.plot(sizes, linear_times, label='Linear Search')
plt.plot(sizes, binary_times, label='Quicksort + Binary Search')
plt.legend(loc='best')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Performance Comparison (Worst-Case Quicksort)')
plt.savefig('ex6_worst.png')
plt.show()
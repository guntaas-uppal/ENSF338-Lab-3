import sys 
sys.setrecursionlimit(20000)

import time
import matplotlib.pyplot as plt
import numpy as np

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
    if start > end:
        return start
    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr, key, 0, i-1)
        arr = arr[:j] + [key] + arr[j:i] + arr[i+1:]
    return arr

def measure_execution_time(sort_function, array):
    start_time = time.time()
    if sort_function == binary_insertion_sort:
        sorted_array = sort_function(array.copy())
    else:
        sort_function(array.copy())
    end_time = time.time()
    return end_time - start_time

input_sizes = np.arange(10, 1001, 50)  # From 10 to 1000 with steps of 50
times_insertion = []
times_binary_insertion = []

for size in input_sizes:
    array = np.random.randint(low=0, high=10000, size=size)
    times_insertion.append(measure_execution_time(insertion_sort, array))
    times_binary_insertion.append(measure_execution_time(binary_insertion_sort, array))

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, times_insertion, label='Traditional Insertion Sort', marker='o')
plt.plot(input_sizes, times_binary_insertion, label='Binary Insertion Sort', marker='x')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Insertion Sort vs. Binary Insertion Sort Performance')
plt.legend()
plt.grid(True)
plt.show()

# Discussion of Results:
# This section should contain comments analyzing the results from the plot.
# It will discuss which algorithm is faster and theorize why this is the case, considering both the number of comparisons and the overhead involved.
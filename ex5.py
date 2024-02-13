import time
import numpy as np
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def binary_search(arr, val, start, end):
    if start == end:
        return start if arr[start] > val else start + 1
    if start > end:
        return start
    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        pos = binary_search(arr, key, 0, i-1)
        while i > pos:
            arr[i] = arr[i-1]
            i -= 1
        arr[pos] = key
    return arr

def measure_time(func, arr):
    start = time.time()
    func(arr)
    end = time.time()
    return end - start

input_sizes = [10, 50, 100, 150, 200, 250, 300]
times_insertion = []
times_binary = []

for size in input_sizes:
    arr = np.random.randint(0, 10000, size).tolist()
    times_insertion.append(measure_time(insertion_sort, arr.copy()))
    times_binary.append(measure_time(binary_insertion_sort, arr.copy()))

plt.figure(figsize=(10, 5))
plt.plot(input_sizes, times_insertion, label='Insertion Sort', marker='o')
plt.plot(input_sizes, times_binary, label='Binary Insertion Sort', marker='x')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Performance Comparison')
plt.legend()
plt.grid(True)
plt.show()


#Question 4:
'''
Theoretically, binary insertion sort reduces the number of comparison counts by finding insertion points using binary search. It may also 
offer performance benefits compared to traditional insertion sort especially for large data sets. Practically, however, the benefits may 
be minimal in average-case cases due to the underlying operation costs. Both algorithms carry out element shifts, keeping the complexity 
of the rearrangement relatively low. However, binary search's overhead may offset comparison savings. This is especially true in higher-level 
languages, where array manipulation is expensive. While binary insertion sort does optimise comparisons, the overall performance advantage 
of binary insertion sort vs. traditional insertion sort becomes more noticeable only under certain conditions or with larger data sets.
'''


import time
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [pivot], []
        for x in arr[:-1]:
            if x < pivot:
                smaller.append(x)
            elif x > pivot:
                larger.append(x)
            else:
                equal.append(x)
        return quicksort(smaller) + equal + quicksort(larger)

def measure_worst_case(input_sizes):
    times = []
    for size in input_sizes:
        # Generating a worst-case scenario vector (sorted in ascending order)
        arr = list(range(1, size + 1))
        start_time = time.time()
        quicksort(arr)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

input_sizes = [10, 50, 100, 200, 300, 400, 500]
times = measure_worst_case(input_sizes)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, times, marker='o', linestyle='-', color='b')
plt.title('Quicksort Execution Time in Worst-Case Scenario')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()

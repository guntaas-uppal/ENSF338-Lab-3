import sys 
import time
import random
import matplotlib.pyplot as plt
import numpy as np
sys.setrecursionlimit(200000)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1) 
        quicksort(arr, pivot_index + 1, high)
    return arr

def generate_bubble_list_case(arr, case_type):
    sorted_values = sorted(arr)
    if case_type == "best":
        start_time = time.time()
        bubble_sort(sorted_values)
        return time.time() - start_time
    elif case_type == "worst":
        start_time = time.time()
        sorted_values.reverse()
        bubble_sort(sorted_values)
        return time.time() - start_time
    elif case_type == "avg":
        start_time = time.time()
        bubble_sort(arr)
        return time.time() - start_time

def generate_quicksort_list_case(arr, case_type):
    sorted_values = sorted(arr)
    lowest = sorted_values[0]
    middle_index = (len(sorted_values)) // 2
    if (len(sorted_values)) % 2 == 0:
        middle = int((sorted_values[middle_index - 1] + sorted_values[middle_index]) / 2.0)
    else:
        middle = int(sorted_values[middle_index])

    if case_type == "best":
        start_time = time.time()
        quicksort(arr, middle, (len(sorted_values) -1))
        return time.time() - start_time
    elif case_type == "worst":
        arr.sort(reverse=True)
        start_time = time.time()
        quicksort(arr, lowest, (len(sorted_values) -1))
        return time.time() - start_time
    elif case_type == "avg":
        random.shuffle(arr)
        random_num = int(random.randint(0, (len(arr) -1)))
        start_time = time.time()
        quicksort(arr, random_num, (len(sorted_values) -1))
        return time.time() - start_time

def smart_sort(arr, num, case_type):
    if len(arr) < num:
        return generate_bubble_list_case(arr, case_type)
    else:
        return generate_quicksort_list_case(arr, case_type)

def test_algorithm(algorithm, arr, num, case_type):
    if algorithm == "bubble":
        return generate_bubble_list_case(arr, case_type)
    elif algorithm == "quick":
        return generate_quicksort_list_case(arr, case_type)
    elif algorithm == "smart":
        return smart_sort(arr, num, case_type)

input_sizes = [i for i in range(5, 1001, 10)]
times = {alg: {case: [] for case in ['best', 'worst', 'average']} for alg in ['bubble', 'quicksort', 'smart']}
num = 125
for size in input_sizes:
    arr = [random.randint(0, size) for _ in range(size)]
    times['bubble']['best'].append(test_algorithm("bubble", arr, num, "best"))
    times['bubble']['worst'].append(test_algorithm("bubble", arr, num, "worst"))
    times['bubble']['average'].append(test_algorithm("bubble", arr, num, "avg"))

    times['quicksort']['best'].append(test_algorithm("quick", arr, num, "best"))
    times['quicksort']['worst'].append(test_algorithm("quick", arr, num, "worst"))
    times['quicksort']['average'].append(test_algorithm("quick", arr, num, "avg"))

    times['smart']['best'].append(test_algorithm("smart", arr, num, "best"))
    times['smart']['worst'].append(test_algorithm("smart", arr, num, "worst"))
    times['smart']['average'].append(test_algorithm("smart", arr, num, "avg"))

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('Sorting Algorithm Performance by Specific Scenarios')

case_types = ['best', 'worst', 'average']
algorithms = ['bubble', 'quicksort', 'smart']
case_colors = {'bubble': 'blue', 'quicksort': 'orange', 'smart': 'green'}

for j, case in enumerate(case_types):
    for alg in algorithms:
        axes[0, j].plot(input_sizes, times[alg][case], label=f'{alg.capitalize()} {case.capitalize()} case', color=case_colors[alg])
    axes[0, j].set_title(f'{case.capitalize()} Case for Each Algorithm')
    axes[0, j].set_xlabel('Input Size')
    if j == 0:
        axes[0, j].set_ylabel('Time (seconds)')
    axes[0, j].legend()
    axes[0, j].grid(True)


for j, case in enumerate(case_types):
    bubble_times = np.array(times['bubble'][case])
    quicksort_times = np.array(times['quicksort'][case])

    axes[1, j].plot(input_sizes, bubble_times, label='Bubble Sort', color='blue')
    axes[1, j].plot(input_sizes, quicksort_times, label='Quicksort', color='orange')

    axes[1, j].fill_between(input_sizes, 0, bubble_times, where=bubble_times <= quicksort_times, color='blue', alpha=0.1)
    axes[1, j].fill_between(input_sizes, 0, quicksort_times, where=quicksort_times < bubble_times, color='orange', alpha=0.1)

    overall_better = 'Bubble' if np.sum(bubble_times) <= np.sum(quicksort_times) else 'Quicksort'
    axes[1, j].text(0.5, 0.95, f'{overall_better} overall better', transform=axes[1, j].transAxes, 
                    fontsize=10, verticalalignment='top', horizontalalignment='center', 
                    bbox=dict(facecolor='white', alpha=0.8))

    axes[1, j].set_title(f'Bubble vs Quicksort: {case.capitalize()} Case')
    axes[1, j].set_xlabel('Input Size')
    if j == 0:
        axes[1, j].set_ylabel('Time (seconds)')
    axes[1, j].legend()
    axes[1, j].grid(True)

plt.tight_layout()
plt.show()
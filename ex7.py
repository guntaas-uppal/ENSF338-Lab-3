import sys 
import json
import time
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)

def binary_search(arr, target, midpoint):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = midpoint if start == 0 else (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

with open('ex7data.json', 'r') as f:
    data = json.load(f)

with open('ex7tasks.json', 'r') as f:
    tasks = json.load(f)

first_midpoint = len(data) // 2
for target in tasks:
    index = binary_search(data, target, first_midpoint)
    print(f'Target: {target}, Index: {index}')

plt.xlabel('Target')
plt.ylabel('Best Midpoint')
plt.title('Best Midpoint for Each Target')
targets_list = []
midpoints_list = []

for target in tasks:
    time_ = float('inf')
    midpoint_ = None
    for midpoint in range(len(data)):
        start_time = time.time()
        binary_search(data, target, midpoint)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time < time_:
            time_ = elapsed_time
            midpoint_ = midpoint
    targets_list.append(target)
    midpoints_list.append(midpoint_)

    print(f'Target: {target}, Best Midpoint: {midpoint_}, Best Time: {time_}')
plt.scatter(targets_list, midpoints_list)
plt.savefig('ex7_plot.png')
plt.show()
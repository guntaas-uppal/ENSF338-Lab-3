import random 
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    num_comparisons = 0
    num_swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            num_comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                num_swaps += 1
    return num_comparisons, num_swaps

def main():
    input_sizes = [10, 20, 50, 100, 200, 500]
    for size in input_sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]
        comparisons, swaps = bubble_sort(arr)
        print(f"Input Size: {size}, Comparisons: {comparisons}, Swaps: {swaps}")

# Plotting the results
plt.figure(figsize=(14, 6))

# Plotting number of comparisons
plt.subplot(1, 2, 1)
plt.plot(input_sizes, num_comparisons, marker='o', linestyle='-', color='b', label='Comparisons')
plt.title('Number of Comparisons by Input Size')
plt.xlabel('Input Size')
plt.ylabel('Number of Comparisons')
plt.grid(True)
plt.legend()

# Plotting number of swaps
plt.subplot(1, 2, 2)
plt.plot(input_sizes, num_swaps, marker='o', linestyle='-', color='r', label='Swaps')
plt.title('Number of Swaps by Input Size')
plt.xlabel('Input Size')
plt.ylabel('Number of Swaps')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

if __name__ == "__main__":
    main()
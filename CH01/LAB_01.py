import time
import math

def linear_search(arr, item):
    """
    Performs linear search on an array.
    Returns the index if found, None otherwise.
    """
    # Loop through each element in the array
    for i in range(len(arr)):
        # Compare each element with the target item
        if arr[i] == item:
            # Return the index when found
            return i
    # Return None if not found
    return None

def binary_search(arr, item):
    """
    Performs binary search on a sorted array.
    Returns the index if found, None otherwise.
    """
    # Set low and high boundaries
    low = 0
    high = len(arr) - 1
    
    # Continue searching while the range is valid
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        guess = arr[mid]
        
        # Check if we found the item
        if guess == item:
            return mid
        # If guess is too high, search the lower half
        elif guess > item:
            high = mid - 1
        # If guess is too low, search the upper half
        else:
            low = mid + 1
    
    # Return None if item not found
    return None

def time_search_comparison(arr, target):
    """
    Times both search algorithms and returns the results.
    Returns a tuple of (linear_time, binary_time, linear_result, binary_result)
    """
    # Time linear search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Time binary search
    start_time = time.time()
    binary_result = binary_search(arr, target)
    binary_time = time.time() - start_time
    
    return linear_time, binary_time, linear_result, binary_result

# Main execution with hardcoded data
if __name__ == "__main__":
    # Create a sorted list of 128 names (using numbers for simplicity)
    sorted_names = list(range(1, 129))  # [1, 2, 3, ..., 128]
    
    # Test cases - searching for different items
    test_items = [1, 64, 128, 50, 100, 25, 75, 10, 90, 200]  # 200 is not in the list
    
    print("Binary Search vs Linear Search Time Comparison")
    print("================================================")
    print("Searching in a sorted list of 128 numbers")
    print()
    
    for item in test_items:
        linear_time, binary_time, linear_result, binary_result = time_search_comparison(sorted_names, item)
        
        print(f"Searching for: {item}")
        print(f"Linear search time: {linear_time:.8f} seconds")
        print(f"Binary search time: {binary_time:.8f} seconds")
        print(f"Linear search result: {linear_result}")
        print(f"Binary search result: {binary_result}")
        
        if linear_time > 0 and binary_time > 0:
            speedup = linear_time / binary_time
            print(f"Binary search is {speedup:.2f}x faster")
        print()
    
    # Answer the lab challenge question
    print("Lab Challenge Answer:")
    print("Maximum steps for binary search in 128 items:")
    max_steps = math.ceil(math.log2(128))
    print(f"log2(128) = {max_steps} steps maximum")

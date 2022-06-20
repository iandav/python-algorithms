# Bubble Sort O(n^2)
def bubble_sort(nums):
    # Create a copy of the list, to avoid changing it
    nums = list(nums)
    
    # 4. Repeat the process n-1 times
    for _ in range(len(nums) - 1):
        
        # 1. Iterate over the array (except last element)
        for i in range(len(nums) - 1):
            
            # 2. Compare the number with  
            if nums[i] > nums[i+1]:
                
                # 3. Swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    # Return the sorted list
    return nums

print("Bubble sort of [2,1,4,3,5]:", bubble_sort([2,1,4,3,5]))

# Insertion Sort: O(n^2)
def insertion_sort(nums):
    index_range = range(1, len(nums))
    # Iterate over the array (except first element)
    for i in index_range:
        value_to_sort = nums[i]
        # Compare the actual value with the left element
        while nums[i-1] > value_to_sort and i > 0:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i -= 1
    return nums
        
print("Insertion sort of [2,1,4,3,5]:", insertion_sort([2,1,4,3,5]))

# Merge Sort (n*log(n))
# 1. If the input list is empty or contains just one element, it is already sorted. Return it.
# 2. If not, divide the list of numbers into two roughly equal parts.
# 3. Sort each part recursively using the merge sort algorithm. You'll get back two sorted lists.
# 4. Merge the two sorted lists to get a single sorted list

# Create a function to merge 2 sorted arrays
def merge(list_1, list_2):
    # Result of merged lists
    merged = []

    # Define indices
    i, j = 0, 0

    # Include the smaller element in the result and move to next element
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            merged.append(list_1[i])
            i += 1
        else:
            merged.append(list_2[j])
            j += 1
    
    # Include the remainder elements
    list_1_tail = list_1[i:]
    list_2_tail = list_2[j:]

    # Return the merged array with the remainders
    return merged + list_1_tail + list_2_tail

print("Merge 2 sorted arrays:", merge([1,3,5], [2,6,10]))

# Create merge sort
def merge_sort(nums):
    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums
    
    # Get the midpoint
    mid = len(nums) // 2
    
    # Split the list into two halves
    left = nums[:mid]
    right = nums[mid:]
    
    # Solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    
    # Combine the results of the two halves
    sorted_nums =  merge(left_sorted, right_sorted)
    
    return sorted_nums

print("Merge sort of [2,1,4,3,5]", merge_sort([2,1,3,4,5]))

# Quicksort O(n^2)
# 1. If the list is empty or has just one element, return it. It's already sorted.
# 2. Pick a random element from the list. This element is called a pivot.
# 3. Reorder the list so that all elements with values less than or equal to the pivot come before the pivot, while all elements with values greater than the pivot come after it. This operation is called partitioning.
# 4. The pivot element divides the array into two parts which can be sorted independently by making a recursive call to quicksort.

def quick_sort(sequence):
    length = len(sequence)
    if length < 1:
        return sequence
    else:
        pivot = sequence.pop() # It returns the last element

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print("Quick sort of [2,1,4,3,5]", quick_sort([2,1,3,4,5]))
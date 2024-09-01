def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # Check if x is present at mid
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return True

    return False

# Test cases
print(binary_search([1, 2, 3, 5, 8], 6))  # False
print(binary_search([1, 2, 3, 5, 8], 5))  # True


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Sample data
data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
print(quick_sort(data))  # [13, 22, 29, 37, 46, 49, 52, 56, 71]

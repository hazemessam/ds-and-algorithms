def binary_search(arr, target, start_idx=0, end_idx=None):
    if end_idx is None: end_idx = len(arr) - 1

    mid_idx = (start_idx + end_idx) // 2
    if start_idx > end_idx: return -1
    if arr[mid_idx] == target: return mid_idx

    if arr[mid_idx] < target:
        return binary_search(arr, target, mid_idx+1, end_idx)
    else: return binary_search(arr, target, start_idx, mid_idx-1)


print(binary_search([1, 2, 3, 4, 5, 10], 10) == 5)
print(binary_search([1, 2], 1) == 0)
print(binary_search([1, 2], 2) == 1)
print(binary_search([5], 5) == 0)
print(binary_search([], 5) == -1)

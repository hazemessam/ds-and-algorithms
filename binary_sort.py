def search(arr, target, start=0, end=None):
    if end is None: end = len(arr) - 1
    mid_idx = int((start + end) / 2)
    if start > end: return -1
    if arr[mid_idx] == target: return mid_idx
    elif arr[mid_idx] < target: return search(arr, target, mid_idx+1, end)
    else: return search(arr, target, 0, mid_idx-1)


print(search([1, 2, 3, 4, 5, 10], 10))
print(search([1, 2], 1))
print(search([5], 5))
print(search([], 5))
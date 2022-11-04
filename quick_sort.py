from random import randint


def qsort(arr: list) -> list:
    if len(arr) <= 2:
        if len(arr) == 2 and arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    pivot_idx = randint(0, len(arr)-1)
    pivot = arr[pivot_idx]
    left_sub_arr = []
    right_sub_arr = []

    for idx in range(len(arr)):
        if idx == pivot_idx: continue
        if arr[idx] <= pivot: left_sub_arr.append(arr[idx])
        else: right_sub_arr.append(arr[idx])

    return qsort(left_sub_arr) + [pivot] + qsort(right_sub_arr)


print(qsort([1, 2, 3, 4, 6, 7, 8]))
print(qsort([1, 6, 3, 4, 5]))
print(qsort([]))
print(qsort([1]))
print(qsort([5, 7, 1, 0]))
print(qsort([1, 2, 3, 5, 2]))

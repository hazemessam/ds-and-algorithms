def get_min_num_idx(arr: list) -> int:
    min_num_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_num_idx]:
            min_num_idx = i
    
    return min_num_idx


def selection_sort(arr: list) -> list:
    sorted_arr = []
    
    for i in range(len(arr)):
        min_num_idx = get_min_num_idx(arr)
        sorted_arr.append(arr.pop(min_num_idx))
    
    return sorted_arr


print([])
print([1])
print(selection_sort([1, 2, 3]))
print(selection_sort([1, 2, 4, 5, 3]))
print(selection_sort([5, 2, 4, 3, 1]))
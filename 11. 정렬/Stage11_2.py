import sys


def merge_sort(num_arr):
    if len(num_arr) < 2:
        return num_arr

    mid = len(num_arr)//2
    left_arr = merge_sort(num_arr[:mid])
    right_arr = merge_sort(num_arr[mid:])
    merged_arr = list()
    left = right = 0

    while left < len(left_arr) and right < len(right_arr):
        if left_arr[left] < right_arr[right]:
            merged_arr.append(left_arr[left])
            left += 1
        else:
            merged_arr.append(right_arr[right])
            right += 1

    # Add remainder of left_arr and right_arr
    merged_arr += left_arr[left:]
    merged_arr += right_arr[right:]
    print(merged_arr)
    return merged_arr


def heap_sort(num_arr):
    len_arr = len(num_arr)

    # Make a max heap
    for i in range(len_arr):
        heapify(num_arr, i, len_arr)

    # Sorting a heap
    for i in reversed(range(len_arr)):
        num_arr[0], num_arr[i] = num_arr[i], num_arr[0]
        heapify(num_arr, 0, i)

    return num_arr


def heapify(arr, index, heapsize):
    largest = index
    # index == root
    left_idx = 2*index + 1
    right_idx = 2*index + 2
    if left_idx < heapsize and arr[left_idx] > arr[largest]:
        largest = left_idx
    if right_idx < heapsize and arr[right_idx] > arr[largest]:
        largest = right_idx
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, heapsize)

    # print(arr)


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    num_list = list()

    for _ in range(N):
        num_list.append(int(sys.stdin.readline().rstrip()))

    # sorted_list = merge_sort(num_list)
    # print(*sorted_list)
    # Be aware; algorithm of heap sort is not that clear
    # sorted_list = heap_sort(num_list)
    # print(*sorted_list)

    print(*sorted(num_list))
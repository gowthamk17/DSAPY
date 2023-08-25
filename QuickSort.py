def quick_sort(array, start, end):
    if start < end:
        pi = partition(array, start, end)
        quick_sort(array, start, pi - 1)
        quick_sort(array, pi + 1, end)

def partition(array, start, end):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
        while end > pivot_index and array[end] >= pivot:
            end -= 1
        if start <= end:
            swap(array, start, end)
        
    swap(array, pivot_index, end)

    return start

def lomuto_partition(array, start, end):
    pivot = array[end]
    j = start
    i = start - 1
    while j < end:
        while array[j] >= pivot and j < end:
            j += 1
        i += 1
        swap(array, i, j)
        j += 1
    i += 1
    swap(array, i, end)

    return i


def swap(array, a, b):
    if a != b:
        temp = array[a]
        array[a] = array[b]
        array[b] = temp


if __name__ == '__main__':
    elements = [7, 2, 4, 6, 9, 1, 8, 3, 5]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)
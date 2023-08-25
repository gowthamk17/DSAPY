def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[mid:]
    right = array[:mid]
    merge_sort(left)
    merge_sort(right)
    merge_two_arrays(left, right, array)

def merge_two_arrays(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    while i < len_a and j < len_b:
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

if __name__ == '__main__':
    elements = [7, 2, 4, 6, 9, 1, 8, 3, 5]
    print(elements)
    merge_sort(elements)
    print(elements)
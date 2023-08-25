def selection_start(arr):
    size = len(arr)
    for i in range(size - 1):
        min_index = i
        for j in range(i+1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == '__main__':
    elements = [7, 2, 4, 6, 9, 1, 8, 3, 5]
    selection_start(elements)
    print(elements)
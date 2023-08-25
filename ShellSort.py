def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        gap //= 2


if __name__ == '__main__':
    elements = [7, 2, 4, 6, 9, 1, 8, 3, 5]
    shell_sort(elements)
    print(elements)
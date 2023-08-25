def bubble_sort(unsorted_list):
    size = len(unsorted_list)
    for k in range(size - 1):
        swapped = False
        for i in range(size - 1 - k):
            if unsorted_list[i] > unsorted_list[i + 1]:
                tmp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i + 1]
                unsorted_list[i + 1] = tmp
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    number_list = [7, 6, 2, 8, 9, 1, 4]
    bubble_sort(number_list)
    print(number_list)

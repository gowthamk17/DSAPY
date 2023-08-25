def insetion_sort(array):
    for i in range(1, len(array)):
        anchor = array[i]
        j = i - 1
        while j >= 0 and array[j] > anchor:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = anchor



if __name__ == '__main__':
    elements = [7, 2, 4, 6, 9, 1, 8, 3, 5]
    insetion_sort(elements)
    print(elements)
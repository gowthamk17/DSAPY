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

def bubble_sort_by_key(unsorted_list, key=None):
    size = len(unsorted_list)
    for j in range(size - 1):
        swapped = False
        for i in range(size - 1 - j):
            a = unsorted_list[i][key]
            b = unsorted_list[i+1][key]
            if a > b:
                tmp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i+1]
                unsorted_list[i+1] = tmp
                swapped = True
        if not swapped:
            break;


if __name__ == '__main__':
    number_list = [7, 6, 2, 8, 9, 1, 4]
    bubble_sort(number_list)
    print(number_list)
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    bubble_sort_by_key(elements, 'name')
    print(elements)
def binary_search(number_list, target):
    left = 0
    right = len(number_list) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if number_list[mid] == target:
            return mid
        elif number_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(number_list, target, left, right):
    if left <= right:
        mid = left + (right - left) // 2
        if number_list[mid] == target:
            return mid
        elif number_list[mid] < target:
            return binary_search_recursive(number_list, target, mid + 1, right)
        else:
            return binary_search_recursive(number_list, target, left, mid - 1)
    else:
        return -1


if __name__ == '__main__':
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 4
    print(f"Binary Search Index of {target} is {binary_search(number_list, target)}")
    print(f"Binary Search Recursive of {target} is {binary_search_recursive(number_list, target, 0, len(number_list) - 1)}")
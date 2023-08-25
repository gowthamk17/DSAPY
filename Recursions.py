def find_sum_iter(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum

def find_sum_recur(num):
    if num == 1:
        return 1
    return num + find_sum_recur(num-1)


if __name__ == '__main__':
    print(find_sum_iter(100))
    print(find_sum_recur(100))
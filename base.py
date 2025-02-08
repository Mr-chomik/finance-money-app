def fibonacci(stop_num):
    if stop_num <= 1:
        print("Error")

    elif stop_num == 2:
        print(1)
        print(1)

    else:
        last_num = 1
        before_last_num = 1
        while last_num <= stop_num:
            last_num = last_num + before_last_num
            before_last_num = last_num - before_last_num
            print(before_last_num)


#fibonacci(int(input()))


def bubble_sort(list_sort):
    n = len(list_sort)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list_sort[j] > list_sort[j + 1]:
                list_sort[j], list_sort[j + 1] = list_sort[j + 1], list_sort[j]

    return list_sort


#print(bubble_sort(list(map(lambda elem: int(elem), input().split()))))


def len_sort(list_sort):
    n = len(list_sort)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if len(list_sort[j]) > len(list_sort[j + 1]):
                list_sort[j], list_sort[j + 1] = list_sort[j + 1], list_sort[j]

    return list_sort


#print(len_sort(input().split()))
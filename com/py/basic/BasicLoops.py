def loop_thru_list(numbers):
    print("loop stats")
    for i in numbers:
        print(i)
    print("loop ends")


def loop_thru_using_range_func(numbers):
    # print elements from start to last index
    print("loop stats")
    for i in range(numbers.__len__()):
        print(numbers[i])
    print("loop ends")

    # print elements from start to last index
    print("loop stats")
    for i in range(len(numbers)):
        print(numbers[i])
    print("loop ends")

    # print elements from-to provided index
    print("loop stats")
    for i in range(2, 4):
        print(numbers[i])
    print("loop ends")

    # print elements from-to provided index with incremental value provided
    print("loop stats")
    for i in range(0, 5, 2):
        print(numbers[i])
    print("loop ends")


list1 = [1, 2, 3, 4, 5]

loop_thru_list(list1)
loop_thru_using_range_func(list1)

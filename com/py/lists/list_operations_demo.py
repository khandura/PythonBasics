# create global lists
list_of_fruits = ['Apple', 'Mango', 'Peach']
list_of_countries = ['India', 'Switzerland', 'America']


def access_element_from_list():
    # access element by providing index
    print(f'list of fruits {list_of_fruits}')
    print(f'second element of list of fruits : {list_of_fruits[1]}')

    # access element by providing index
    print(f'first and second elements of fruit list : {list_of_fruits[0:2]}')

    my_list = [num for num in range(1, 11)]
    print("number lis : ", my_list)

    # elements 3rd to 5th
    print('my_list[2:5])', my_list[2:5])

    # elements beginning to 4th
    print('my_list[:-5]', my_list[:-5])

    # elements 6th to end
    print('my_list[5:]', my_list[5:])

    # elements 6th to end
    print('my_list[:]', my_list[-5:])

    # elements 6th to end
    # print('out of bound element : my_list[14]', my_list[14])  //will throw IndexError: list index out of range exception


def list_min_max_elements():
    nums = [num for num in range(1, 10)];
    print(f'numbers : {nums}')
    print(f'length of nums : {len(nums)}')
    print(f'max number in nums : {max(nums)}')
    print(f'min number in nums : {min(nums)}')
    print(f'sum of numbers in nums : {sum(nums)}')


def add_element_to_list():
    nums1 = [1, 2, 3, 4]
    print(f'list  : {nums1}')
    nums1.append(10)
    print(f'list after adding 10 to it  nums1.append(10) : {nums1}')
    nums1.extend([11, 12, 13])
    print(f'list after adding 11, 12, 13 to it  nums1.extend([11, 12, 13]) : {nums1}')
    nums1.insert(0, 14)
    print(f'list after adding 14 to it  nums1.insert(0, 14) : {nums1}')
    nums1[0:1] = [0, 0]
    print(f'list after adding 15, 16 to it  nums1[0:1] = [0, 0] : {nums1}')


def remove_element_from_list():
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'list  : {nums1}')
    nums1.remove(1)  # removes the value from the list, argument is the actual value not the index
    print(f'list after removing value 1  nums1.remove(1) : {nums1}')
    nums1.pop()
    print(f'list after removing last element nums1.pop() : {nums1}')
    nums1.pop(5)
    print(f'list after removing 5th index element nums1.pop(5) : {nums1}')
    del nums1[0]
    print(f'list after removing first element del nums1[0] : {nums1}')
    del nums1[2:5]
    print(f'list after removing 2nd 3rd and 4th element del nums1[2:5] : {nums1}')


def combine_lists():
    nums1 = [1, 2, 3, 4]
    nums2 = [5, 6, 7, 8, 9]
    print(f'list1  : {nums1}')
    print(f'list2  : {nums2}')
    nums3 = nums1 + nums2
    print(f'list after merge nums3 = nums1 + nums2 : {nums3} ')
    nums1.extend(nums2)
    print(f'list after merge  nums1.extend(nums2) : {nums1} ')


def index_type_error():
    nums = [1, 2, 3, 4]
    print('list : ', nums)
    print('passing string as index : ', nums['1'])


def traverse_list():
    nums = [1, 2, 3, 4, 5]
    print('nums : ', nums)
    for num in nums:
        print(num)


def misc_list_operations():
    names = ['Ak', 'Pk', 'Ps', 'Ac', 'Pk']
    print(f'names list : {names}')

    # find the index of an object
    print('index of Pk : ', names.index("Pk"))
    # print('index of unknown object : ', names.index("UK"))    #unkown value will throw ValueError

    # find the number of occurrences of an object
    print('occurrences of Pk : ', names.count('Pk'))

    # check if list contains an object
    print('names contains Pk ', 'Pk' in names)
    print('names contains Pk ', 'Pk' not in names)


def sorting_and_reversing_list():
    names = ['Ak', 'Pk', 'P', 'Ack', 'Pk']
    print(f'names list : {id(names)} , {names}')

    # sorting list
    print(f'sorted list {id(names.sort(key=len))} {names}')
    print(f'sorted list {id(names.sort(key=len))} {names}')

    names = ['Ak', 'Pk', 'P', 'Ack', 'Pk']
    print(f'names list : {id(names)} , {names}')
    sorted(names)
    print(names)


# access_element_from_list()
# list_min_max_elements()
# add_element_to_list()
# remove_element_from_list()
# combine_lists()
# index_type_error()
# traverse_list()
# misc_list_operations()
sorting_and_reversing_list()

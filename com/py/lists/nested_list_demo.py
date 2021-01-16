def create_and_traverse_nested_list():
    names = ['Ak', 'PK']
    fruits = ['Apple', 'Mango']
    nums = [x for x in range(5)]
    print('names :', names)
    print('fruits :', fruits)
    print('nums :', nums)

    # create nested list
    nest_list = [names, fruits, nums, ['aa', 'bb'], 'last element']
    print('nested list :', nest_list)

    # access nested list elements
    # access fruits
    print('fruits :', nest_list[1])
    print('Mango in fruits :', nest_list[1][1])

    dic = {'name': 'Akhilesh', 'profile': 'Python Dev'}
    nest_list.append(dic)
    print(nest_list)
    print(nest_list[-1].get('name'))


create_and_traverse_nested_list()

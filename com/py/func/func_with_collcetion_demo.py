def func_modify_coll(list):
    """each param object is passed by reference,
    updating structure of it will be reflected outside of the function as well"""
    for item in list:
        print(item)
    list.append('Abc')


names = ['Rama', 'Dave']
print(f'names before {names}')
func_modify_coll(names)
print(f'names after {names}')



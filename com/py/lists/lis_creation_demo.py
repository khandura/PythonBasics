# list creation using []
names = ['A', 'BC', 'MC']
print(f'names {names}')

# list creation using range()
nums = [num for num in range(2, 10)]
print(f'nums {nums}')

# list creation using list()
fruits = list()
fruits.append('apple')
fruits.append('orange')
fruits.append('mango')
print(f'fruits {fruits}')

# list creation using list()
list1 = list('WORLD')
print(f'list1 {list1}')


# list creation using list()
list1 = list(['WORLD', 'GONNA', 'END'])
print(f'list1 {list1}')

# both the empty list will be equal
a = []
b = list()

print(a == b)
print(a.__eq__(b))

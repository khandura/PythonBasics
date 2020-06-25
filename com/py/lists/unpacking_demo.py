list = [1, 2, 3]
print(list)

x, y, z = list
print(f'{x}, {y}, {z}')

# below code will throw error, too many values to unpack (expected 2)
a, b = list
print(f'{a}, {b}')

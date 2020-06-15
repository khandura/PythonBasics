# this program demonstrates the different variable scopes.

def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10

print('a =', a)
outer_function()
print('a =', a)


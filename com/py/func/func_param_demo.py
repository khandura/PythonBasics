"""functions to show usage of parameters"""

name = 'Global Name'


def func_with_no_var():
    name = 'rocky'
    print(f'hello {name}')


def func_with_local_var(name):
    print(f'hello {name}')


def func_updating_global_var():
    global name
    name = 'Rocky'
    print(f'hello {name}')


func_with_local_var('AK')
print(f'global name before {name}')
func_with_no_var()
print(f'global name after {name}')

print(f'global name before {name}')
func_updating_global_var()
print(f'global name after {name}')

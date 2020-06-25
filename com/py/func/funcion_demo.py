import math


# function without arguments
def no_arg_func():
    print("No arg function")


def one_arg_func(name):
    print(f'Hello {name} have a good day!')


def func_with_default_arg(name='User'):
    print(f'Hello {name} have a good day!')


def func_with_return_val(num1, num2):
    return num1 + num2


def fun_return_none():
    print('every python method returns None be default')


def func_with_mult_args(name, age, profile='NA'):
    print(f'hello {name} you are {age} old and your profile is {profile}')


# default params should be placed at the end, else it will throw error
# def func_with_default_args_first(profile='NA', name):
#     print(f'hello {name} you are a {profile}')


no_arg_func()
one_arg_func("Akhilesh")
func_with_default_arg()
sum = func_with_return_val(10.5, 12.5)
print(f'sum : {sum}')
nothing = fun_return_none()
print(nothing is None)
func_with_mult_args('Akhilesh', 32, 'Java Dev')

# call function by arg name
func_with_mult_args(age=32, profile='Python Dev', name='Rocky')
# func_with_default_args_first('Akhi')

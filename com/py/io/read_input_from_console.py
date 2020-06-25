# code to demonstrate reading input from console


def read_data_from_console():
    name = input('Enter your name : ')
    profile = input('Enter your profile : ')
    salary = input('Enter your salary : ')

    # string_formatting_plain_print(name, profile, salary)

    # string_formatting_with_format_method(name, profile, salary)

    string_formatting_with_f(name, profile, salary)


def string_formatting_plain_print(name, profile, salary):
    # string format way1
    print('hey', name, 'you are earning', salary, 'as a', profile)
    print('hey', name, 'you are earning', salary * 2, 'as a',
          profile)  # alary will be treated as string and will be printed two times
    print('hey', name, 'you are earning', float(salary) * 2, 'as a', profile)


def string_formatting_with_format_method(name, profile, salary):
    # string format way2
    # if you don't mention the index default will order will be picked
    print('hey {} you are earning {} as a {}'.format(name, salary, profile))
    print('hey {} you are earning {} as a {}'.format(name, salary * 2, profile))
    print('hey {} you are earning {} as a {}'.format(name, float(salary) * 2, profile))
    # you can also specify the index of variables
    print('hey {0} you are a {2} and earning {1} monthly!'.format(name, float(salary) * 2, profile))
    # you can also specify how many floating points you want to display
    print('hey {0} you are a {2} and earning {1:.3f} monthly!'.format(name, float(salary) * 2, profile))


def string_formatting_with_f(name, profile, salary):
    print(f'hey {name} you are earning {salary} as a {profile}')
    print(f'hey {name} you are earning {salary * 2} as a {profile}')
    print(f'hey {name} you are earning {float(salary) * 2} as a {profile}')
    # print(f'hey {name} you are earning {float(salary * 2)}:.3f as a {profile}')    //will throw error
    print(f'hey {name} you are a {profile} and earning {float(salary) * 2:.3f} monthly!')


read_data_from_console()

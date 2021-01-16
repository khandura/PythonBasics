from com.py.decorators.employee_records import Employee
from datetime import datetime


# example-1: decorator with annotation and without argument
def print_name_decorator(caller_func):
    print('print_name_decorator begins')

    def wrapper_method():
        return caller_func()

    return wrapper_method


def print_name():
    print(f'print_name starts')
    print("Welcome to decorator demo")


dd = print_name_decorator(print_name)
print(f'type of dd {dd}')
dd()


# example-2: decorator function with arguments
def decorator_func_with_args(caller_func):
    print('executing decorator_func_with_args method')

    def wrapper_func(*args, **kwargs):
        print('executing wrapper_func')
        return caller_func(*args, **kwargs)

    return wrapper_func


def print_args_func(name, profile):
    print('executing print_args_func')
    print(f'name : {name} - profile : {profile}')


decp = decorator_func_with_args(print_args_func)
decp('Akhilesh', 'Java Dev')


# example-3 : most convenient approach, calling decorator function with annonation
def employee_decorator_func(func_to_be_called):
    print(f'executing employee_decorator_func - {employee_decorator_func.__name__}')

    def wrapper_func(*args, **kwargs):
        print(f'executing wrapper_func - {wrapper_func.__name__}')
        return func_to_be_called(*args, **kwargs)

    return wrapper_func


def display_employee_sorted_by_joining_date(employees):
    print(f'executing display_employee_sorted_by_joining_date - {display_employee_sorted_by_joining_date.__name__}')
    print('employee list')
    Employee.print_employee_data(employees)
    se = sorted(employees, key=lambda emp: emp.date_of_joining)
    print('sorted employee by date of joining')
    Employee.print_employee_data(se)


@employee_decorator_func
def sort_employees_by_joining_date(employees):
    """this method calls the another method employee_decorator_func everytime we
     make a call to sort_employees_by_joining_date"""
    print(f'executing sort_employees_by_joining_date - {sort_employees_by_joining_date.__name__}')
    print('employee list')
    Employee.print_employee_data(employees)
    se = sorted(employees, key=lambda emp: emp.date_of_joining)
    print('sorted employee by date of joining')
    Employee.print_employee_data(se)


# emp_data = employee_decorator_func(display_employee_sorted_by_joining_date)

date_formatter = "%Y%m%d"
emp1 = Employee('Akhilesh', 'Java Developer', datetime.strptime('20151102', date_formatter))
emp2 = Employee('Pooja', 'Accountant', datetime.strptime('20180129', date_formatter))
emp3 = Employee('Priyanka', 'Java Developer', datetime.strptime('20190529', date_formatter))
emp4 = Employee('Navil', 'Java Developer', datetime.strptime('20130825', date_formatter))
emp_list = [emp1, emp2, emp3, emp4]
# emp_data(emp_list)

print('calling decorator function using annotations')
emp_data1 = sort_employees_by_joining_date(emp_list)

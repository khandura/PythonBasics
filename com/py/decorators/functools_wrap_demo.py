import functools
from datetime import datetime
import time


def logger_without_functools_wrap(func):
    start_time = datetime.now()
    print(f'executing {logger_without_functools_wrap.__name__} at {start_time}')

    def log_wrapper(*args, **kwargs):
        nonlocal start_time
        start_time = datetime.now()
        print(f'started executing wrapper {log_wrapper.__name__} at {start_time}')
        result = func(*args, **kwargs)
        time.sleep(2)
        print(f'total time taken to execute wrapper {log_wrapper.__name__} is {datetime.now() - start_time}')
        return result

    time.sleep(2)
    print(f'total time taken to execute {logger_without_functools_wrap.__name__} is {datetime.now() - start_time}')
    return log_wrapper


def logger_with_functools_wrap(func):
    start_time = datetime.now()
    print(f'executing {logger_with_functools_wrap.__name__} at {start_time}')

    @functools.wraps(func)
    def log_wrapper(*args, **kwargs):
        nonlocal start_time
        start_time = datetime.now()
        print(f'started executing wrapper {log_wrapper.__name__} at {start_time}')
        result = func(*args, **kwargs)
        time.sleep(2)
        print(f'total time taken to execute wrapper {log_wrapper.__name__} is {datetime.now() - start_time}')
        return result

    time.sleep(2)
    print(f'total time taken to execute {logger_with_functools_wrap.__name__} is {datetime.now() - start_time}')
    return log_wrapper


@logger_with_functools_wrap
def loop_through_list(names):
    print(f'started executing actual method {loop_through_list.__name__}')
    for name in names:
        print(name)
    print(f'finished executing actual method {loop_through_list.__name__}')


@logger_without_functools_wrap
def loop_through_data(names):
    print(f'started executing actual method {loop_through_data.__name__}')
    for name in names:
        print(name)
    print(f'finished executing actual method {loop_through_data.__name__}')


name_list = ['akhi', 'rana', 'joye']
# rs = loop_through_list(name_list)
rs = loop_through_data(name_list)

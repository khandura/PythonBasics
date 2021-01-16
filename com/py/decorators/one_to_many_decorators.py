from datetime import datetime


def log_execution_time(func_to_be_called):
    start_time = datetime.now()
    print(f'executing {log_execution_time.__name__} at {start_time}')

    def log_wrapper(*args, **kwargs):
        nonlocal start_time, end_time
        start_time = datetime.now()
        print(f'started executing {log_wrapper.__name__} at {start_time}')
        result = func_to_be_called(*args, **kwargs)
        end_time = datetime.now()
        print(f'finished executing {log_wrapper.__name__} at {end_time}')
        print(f'total time taken to execute {log_wrapper.__name__} is {end_time - start_time}')
        return result

    end_time = datetime.now()
    print(f'finished executing {log_execution_time.__name__} at {end_time}')
    print(f'total time taken to execute {log_execution_time.__name__} is {end_time - start_time}')
    return log_wrapper


@log_execution_time
def loop_through_list(names):
    print(f'executing {loop_through_list.__name__}')
    for name in names:
        print(name)


name_list = ['akhi', 'rana', 'joye']
rs = loop_through_list(name_list)

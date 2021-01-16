from datetime import datetime


class Employee:
    """Employee class: keeps records for all the employees"""

    def __init__(self, name, profile, date_of_joining):
        self.name = name
        self.profile = profile
        self.date_of_joining = date_of_joining

    @staticmethod
    def print_employee_data(emp_list):
        for emp in emp_list:
            print(
                f'employee name : {emp.name.rjust(10, " ")} \t employee profile : {emp.profile.rjust(20, " ")} \t '
                f'employee DOJ : {str(emp.date_of_joining).rjust(20, " ")}')

#
# date_formatter = "%Y%m%d"
# emp1 = Employee('Akhilesh', 'Java Developer', datetime.strptime('20151102', date_formatter))
#
# Employee.print_employee_data([emp1])

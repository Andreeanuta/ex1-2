class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):

    mgr_count = 0 

    def __init__(self, name, salary, departament):
        super().__init__(name, salary)
        self.departament = f"B03_{departament}"
        Manager.mgr_count+=1

    def display_employee(self):
        print("Salary : ", self.salary)

    def display_mgr_count(self):
        print(f"Total number of manager(s) is {Manager.mgr_count}")

# X = 4
# Y = 7

Employee1 = Employee("Maia", 3700)
Employee2 = Employee("Silvia", 1900)



Employee1.display_employee()
Employee2.display_employee()

Employee2.display_emp_count()

ManagerI= []

Manager1 = Manager("Carla", 68000, "departament1")
ManagerI.append(Manager1)
Manager2 = Manager("Andreea", 55000, "departament2")
ManagerI.append(Manager2)



for i in ManagerI:
    i.display_employee()

ManagerI[0].display_emp_count()

ManagerI[0].display_mgr_count()


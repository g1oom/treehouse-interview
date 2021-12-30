import csv

class Worker:
    def __init__(self, id, name, salary, manager_id):
        self.id = id
        self.name = name
        self.salary = salary
        self.manager_id = manager_id

# employee table is stored in text file in csv format
# store employee table into array

employeeArray = ["0"]

with open('q1/employee.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        workerObject = Worker(int(row[0]), row[1], int(row[2]), row[3])
        # worker id corresponds to its index in employeeArray
        employeeArray.append(workerObject)

# -----------------------------------------------------------------
# Part a
nameList = []
# ignore first item in employeeArray
for worker in employeeArray[1:]:
    # exception of employee with no manager
    
    if worker.manager_id != "NULL":
        if worker.salary > employeeArray[int(worker.manager_id)].salary:
            nameList.append(worker.name)

# output
if len(nameList) > 0:
    for name in nameList:
        print(name)


# -----------------------------------------------------------------
# Part b
managerId = []
nonManagerSalary = 0

# store all manager_id to find managers
for worker in employeeArray[1:]:
    if worker.manager_id != "NULL" and int(worker.manager_id) not in managerId:
        managerId.append(int(worker.manager_id))

for index in range(1, len(employeeArray)):
    if index not in managerId:
        nonManagerSalary += employeeArray[index].salary

avgSalary = nonManagerSalary / (len(employeeArray) - 1 - len(managerId))
print("$%.2f" % avgSalary)
class Employee:
    numEmployee = 0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.numEmployee +=1
    def displaycount(self):
        print('total number of employee  {}'.format(Employee.numEmployee))
    def displayemploy(self):
        print(" namae : ", self.name,", salary:  ",self.salary)


emp1=Employee('hafez',100)
emp1.displayemploy()
emp2=Employee("jabed",1000)
emp2.displayemploy()
print("total number of employee are {}".format(Employee.numEmployee))




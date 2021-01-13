
class Employee:
    def __init__(self,id,name,salary,desig):
        self.id=id
        self.name=name
        self.salary=salary
        self.desig=desig

    def __str__(self):
        return self.name
obj=Employee(100,"ajay",25000,"developer")
obj1=Employee(101,"anu",15000,"tester")
obj2=Employee(102,"ay",25000,"developer")

lst=[]
lst.append(obj)
lst.append(obj1)
lst.append(obj2)
upnames=list(map(lambda emp:emp.name.upper(),lst))
print(upnames)

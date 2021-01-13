class Person:
    def set_person(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def print_person(self):
        print("name",self.name)
        print("age",self.age)
        print("gender",self.gender)
obj=Person()
obj.set_person("anu","23","female")
obj.print_person()
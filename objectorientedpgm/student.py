class Student:
    def set_student(self,rol,name,course,total):
        self.rol=rol
        self.name=name
        self.course=course
        self.total=total
    def print_student(self):
        print("rollno",self.rol)
        print("name", self.name)
        print("course", self.course)
        print("total", self.total)
stud=Student()
stud.set_student("1","anu","mca","23")
stud.print_student()
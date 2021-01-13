class Parent:
    def m1(self):
        print("inside parent")


class Child(Parent):
    def m2(self):
        print("inside child")

class Subchild(Child):
    def m3(self):
        print("inside subchild")

sb=Subchild()
sb.m3()
sb.m2()
sb.m1()
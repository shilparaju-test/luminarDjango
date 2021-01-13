class Parent:
    def phone(self):
        print("Have nokia")

class Child(Parent):
    def phone(self):
        print("have iphone")
        
c=Child()
c.phone()

class Parent:
    def phone(self):
        print("have phone")

    def __lap_top(self):
        print("i have lap")

class Child(Parent):
    def bike(self):
        print("bike")

ch=Child()
ch.phone()
ch.bike()
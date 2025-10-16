
class Student:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Rahul", 20)
s2 = Student("Priya", 19)


s1.display()
s2.display()

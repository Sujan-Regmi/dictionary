# OOP Program in Python

# Creating a class
class Student:

    # Constructor
    def __init__(self, name, age, faculty):
        self.name = name
        self.age = age
        self.faculty = faculty

    # Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Faculty:", self.faculty)


# Creating objects
s1 = Student("Sujan", 20, "BCA")
s2 = Student("Ram", 21, "CSIT")

# Calling methods
print("Student 1 Details")
s1.display()

print("\nStudent 2 Details")
s2.display()
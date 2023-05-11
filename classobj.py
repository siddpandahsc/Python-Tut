from inherit import Student

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Person2:
    pass

# name = input('Enter your name: ')
# age = input('Enter your age: ')

# p1 = Person(name, age)
p1 = Person('John', 13)
# del p1.age
print(p1)
print(p1.name)
print(p1.age)

class Person2(Student):
    pass

p1 = Person2()
print(p1.name)
# class MyClass:
#     x=5
#
# obj1 = MyClass()
# print(MyClass.x)
# print(obj1.x)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person("Aarthi", 42)
# print(p1.name, ",", p1.age)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
#
# print(p1)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def __str__(self):
#       return f'{self.name} is {self.age} years old'
#
# p1 = Person("John", 36)
#
# print(p1)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
# p1 = Person("John", 36)
# p1.myfunc()

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#
# p1 = Person("John", 36)
# p1.myfunc()

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#
#   def printname(self):
#     print(self.firstname, self.lastname)
#
# #Use the Person class to create an object, and then execute the printname method:
#
# x = Person("John", "Doe")
# x.printname()

# class Student(Person):
#   pass

# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
#     self.graduationyear = 2019
#
# x = Student("Mike", "Olsen")
# x.printname()
# print(x.graduationyear)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year
#
#
# x = Student("Mike", "Olsen", 2019)
# print(x.firstname, x.lastname, x.graduationyear)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year
#
#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
#
# print(Student("Aarthi", "Vetri", 1999).welcome())

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()

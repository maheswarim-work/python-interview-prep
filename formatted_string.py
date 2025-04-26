age = 10
name = "Bob"

# print(f"My name is {name} and I am {age} years old")

class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"""
            My name is {self.name}.
            I am {self.age + 5} years old
        """

print(A(name, age))

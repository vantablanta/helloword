c = 0
while c < 5:
    print(c)
    c = c + 1

while c < 5:
    c = c + 1
    if c == 3:
        break
    print(c)


# try and except
name1 = "h"
try:
    if name1 > "3":
        print('hi')
finally:     # except isn't working
    print("There is an error here")

# functions


def function_name():
    print('Hello World')


function_name()


def addition_function(num1, num2):
    print(num1 + num2)


addition_function(25, 23)


# inbuilt functions
abs(2)   # returns a  positive number
bool()  # returns either true or false
dir()   # tells you what function can be used with a  specific data type
# help()  # takes ina  function name a tells us what it does
eval("print(5)")  # run python code ins  a string format.. runs a string as a python code
exec("print(5)")  # same as eval but runs more complex code on multiple lines
str()   # converts an integer or float to str
int()   # converts a string or float to int
float()   # converts an integer or string to float

# OOP
# classes ae the overall type.. objects are an instance of that class


class Person:
    pass


p = Person()  # p is an instance of the class Person hence is an object
print(p)


class Person:
    def get_name(self):
        print("Michelle")

    def get_age(self):
        print("16")


p = Person()


p.get_name()
p.get_age()


class Person:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def get_name(self):
        print("Your name is " + self.name)

    def get_age(self):
        print("Your age is " + self.age)


man = Person("25", "Michelle")
man.get_age()
man.get_name()



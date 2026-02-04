#Create a class BankAccount with methods for deposit, withdrawal, balance check, and transaction history.
class BankAccount:
    no_of_users =0
    def __init__(self,name,balance):
        self.__name = name
        self.__balance = balance
        BankAccount.no_of_users +=1
    @classmethod
    def check_count(cls):
        print(cls.no_of_users)
    # def getter(self):
    #     print(self.__name,self.__balance)
    # def setter(self,name,balance):
    #     self.__name = name
    #     self.__balance = balance

# obj = BankAccount("Tarun",1000)
# obj2 = BankAccount("Pravesh",2000)
# obj3 = BankAccount("Sarthak",20000)
# obj4= BankAccount("Darshan",200000)
# obj.check_count()

#Implement a class Circle with property decorators for radius, area, and circumference.
from math import pi
class Circle:
    def __init__(self,radius):
        self._radius = radius
    @property
    def radiuss(self):
        return self._radius
    @radiuss.setter
    def radiuss(self,radius):
        self._radius = radius

    @property
    def area(self):
        return pi* pow(self._radius,2)

    @property
    def circumference(self):
        return 2*pi*self._radius

# cr = Circle(5)
# cr.radiuss = 10
# print(f"{cr.area:.2f}")
# print(f"{cr.circumference:.2f}")


#Write a program that handles multiple exceptions (ValueError, TypeError, FileNotFoundError, ZeroDivisionError).
# try:
#     n = 10
#     # print(10/0)
#     # with open("file.txt",'r') as f:
#     #     f.readlines()
#     # int("four")
#     s = "abc"+n
#     print(s)
# except TypeError:
#     print("Type Error")
#     raise TypeError
# except (ValueError, FileNotFoundError, ZeroDivisionError) as e:
#     print("Error!",e)
# finally:
#     print("executed!")

#Create a base class Animal and derived classes Dog and Cat with method overriding for make_sound()
class Animal:
    def make_sound(self):
        print("Animal making sound!")
class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("dog barking!")
class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print("cat meoww")

# cat = Cat()
# dog = Dog()
# cat.make_sound()
# dog.make_sound()

#Implement a class Stack with push, pop, peek operations and raise custom exceptions for overflow/underflow
class UnderFlow(Exception):
    pass
class Stack():
    lst = []

    def peek(self):
        return Stack.lst[-1]
    def pop(self):
        if len(Stack.lst)<1:
            raise UnderFlow()
        else:
            return Stack.lst.pop()

    def push(self,val):
        if len(Stack.lst)>5:
            raise OverflowError
        else:
            Stack.lst.append(val)

# s1 = Stack()
# s1.push(10)
# s1.push(20)
# s1.push(30)
# s1.push(10)
# s1.push(20)
# s1.push(20)
# print(s1.pop())

#Implement a class with __str__ and __repr__ special methods for better debugging
class Debugging:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} {self.b}"
    def __repr__(self):
        return f"Debugging(a = '{self.a}', b= '{self.b}')"

# d1 = Debugging(10,20)
# print("using __str__",str(d1))
# print("using __repr__",repr(d1))

# Write a context manager class using __enter__ and __exit__ methods to handle database connections or file operations.

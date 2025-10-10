#03/10/2025
#classes and objects
#1 class definition
class MyClass:
    personName = "John"
    personAge = 36
    personCountry = "Norway"
    def MyClassFunction(self): # first parameter is always self for fn in class even if you write something else
        print('MyClassFunction executes')
#2 class object/instance/key creation
myClassObj = MyClass()
print(myClassObj.personName)
myClassObj.MyClassFunction()

#constructors - special function of a class
#points to remember
#1. __init__(), every constructor muse have this name
#2 every class has one constuctor - compiler implicitly creates a default constructor if you do not create one
#3. you call the constructor (not by its name but by class name) while creating the object of the class
class Person:
    #definiing constructor
    def __init__(self,firstName,lastName):
        self.FirstName = firstName #self belongs to constructor
        self.FastName = lastName #self belongs to constructor
        pass
    def PersonFunction(self):
        print('PersonFunction executes')

personObj = Person("ed","sid") #calling init constructor - first line the compiler sees
print(personObj.FirstName)
personObj.PersonFunction()

#why to use constructor - top priority is constructor variables- it executes first

#object oriented programming python, c++, java, c#, javascript (procedural programming c)
#4 topics 
#DRY - do not repeat yourself
#inheritance
#polymorphism
#encapsulation
#abstraction

#inheritance - one class acquires the properties of another class
class Human:
    def __init__(self,firstName,lastName):
        self.FirstName = firstName
        self.LastName = lastName

        def PrintName(self):
            print(self.FirstName,self.LastName)

humanObj = Human("ed","sid")
print(humanObj.FirstName)

class Student(Human): #inheritance
    pass

studentObj = Student('studentFirst','studentLast')


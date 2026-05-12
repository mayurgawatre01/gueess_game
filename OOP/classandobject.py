
#maping real world entities in code 5r
'''class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks > 40:
            print("is Pass by")
        else:
            print("fail")
s1 = Student("Mayur", 90)
s1.result()
s2=Student("mahesh",32)
s2.result()
'''

        
'''class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def check(self):
        if self.price > 50:
            print("Expensive")
        else:
            print("Affordable")

c1 = Car("BMW", 60)
c2 = Car("Maruti", 30)

c1.check()
c2.check()'''

# Q1
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(self.name,self.marks)
s1=Student("mayur",99)
s2=Student("yash",98)
s1.display()
s2.display()
       
#Q2
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>40:
            print("Pass")
        else:
            print("Fail")
s1=Student("onkar",89)
s1.result()

#Q3   
class Car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def discount(self):
        if self.price>50:
            print("High Price")
        else:
            print("Low Price")
c1=Car("AUDI",60)
c1.discount()

#Q4
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def bonus(self):
        if self.salary>50000:
            print(self.name,"salary is :",self.salary+5000)
        else:
            print(self.name,"Salary is :",self.salary+2000)
E1=Employee("mayur",100000)
E2=Employee("Ram",49000)
E1.bonus()
E2.bonus()
E3=Employee("yashraj",90000)
E3.bonus()


name=input("")
salary=int(input(""))
def bonus():
    if salary >50000:
        print(salary+5000)
    else:
        print(salary+2000)
bonus()

    
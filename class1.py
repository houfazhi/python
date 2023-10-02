# 开发时间：2023/8/13 22:42
#类的继承
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name,age,object):
        super().__init__(name,age)
        self.object = object
p = Person("hou",30)
s = Student("fa",21,'computer')
print(p.name,p.age)
print(s.name,s.age,s.object)

#多态
class Animal:
    def eat(self):
        print('动物吃什么')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Person:
    def eat(self):
        print('人吃五谷杂粮')
def fun(obj):
    obj.eat()
fun(Animal())
fun(Dog())
fun(Cat())
fun(Person())
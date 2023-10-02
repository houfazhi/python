# 开发时间：2023/8/13 21:47
#类的知识点
class Student:
    def __init__(self,name,age,salary):
        self.name = name
        self.age  = age
        self.__salary = salary
    def show(self):
        print(self.name,self.age,self.__salary)

s = Student('侯发志',20,9000)
print(s.name,s.age)
#print(s.__salary)  #带__的变量不能直接在外部访问
s.show()

#动态绑定方法和属性
s1 = Student('hou',21,'2w')
s2 = Student('fa',22,'3w')
s1.height = 175 #动态添加s1的属性
s1.show()
print(s1.height)
def speak():
    print('I am speaking')
s2.speak = speak    #动态绑定方法
s2.speak()

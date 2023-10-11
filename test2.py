# 开发时间：2023/8/4 19:27
#字典
print('-----------------字典的创建-------------------')
students = {"hou":20,"li":30}
student = dict( name = "hou",age = 20,score = 90)
print(students); print(student)
print('-----------------字典的查询-------------------')
a = students['hou']
b = students.get("zh",0)
print(a,b,students,type(a),type(b))
c = students.keys()
d = students.values()
e = students.items()
print(c,d,e,type(c),type(d),type(e))
print('-----------------字典的增加-------------------')
students['zhi'] = 50
print(students)
print('-----------------字典的删除-------------------')
del students['li']
print(students)

#list生成式
lst7 = [i*2 for i in range(1,5)]
print(lst7)
#list列表的增删改查操作
print('-----------------list列表的增删改查操作-------------------')
lst3 = [0,10,20,30,40,50]
lst4 = ['hello','world','and','python']
lst5 = ['this','is']
'''增加-1'''
print(lst3)
print("增加操作")
lst3.append(80)
print(lst3)
'''增加-2'''
lst3.extend(lst4)
print(lst3)
'''增加-3'''
lst3.insert(0,'开头')
print(lst3)
'''增加-4'''
lst3[10:11] = lst5
print(lst3)
print("删除操作")
'''删除-1'''
lst3.remove(10)
print(lst3)
'''删除-2'''
lst3.pop(2)
print(lst3)
'''删除-3'''
# lst3[2:4] = []
# print(lst3)
# '''删除-4'''
# lst3.clear()
# print(lst3)
# '''删除-5'''
# del lst3
print(lst3)
print("修改操作")
print(lst3)
lst3[1] = '20'
print(lst3)
lst3[1:3] = [100,200]
print(lst3)
print("列表的排序操作")
lst6 = [21,24,465,23,46,23,465,67,7]
print(lst6)
lst6.sort()
new_lst = sorted(lst6,reverse=True)
print(lst6)
print(new_lst)

#list列表的创建
print('-----------------list列表的创建-------------------')
lst1 = ['abc',123]
lst2 = list(['123','abc'])
print(lst1[-2])
print(lst2[0:2:1])
print(lst1.index('abc'))
#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j),end="\t")
    print()

#循环例题（输入密码问题）

#循环
a = 1
sum = 0
while a<=100:
    if a%2==0:
        sum+=a
    a+=1
print("1-100偶数和为",sum)
fum = 0
for item in range(0,101):
    if item%2==0:
        fum+=item
print(fum)

#range()的三种创建方式
r1 = range(10)
print(r1)
r2 = range(-6,10)
print(r2)
r3 = range(2,8,2)
print(r3)
print(list(r2))
print(4  in r3)
print(2 not in r3)

#条件表达式的应用
num_1 = int(input("请输入第一个数字"))
num_2 = int(input("请输入第2个数字"))
print(str(num_1)+"》="+str(num_2)    if num_1>=num_2 else    str(num_1)+"<"+str(num_2))

#多分枝结构
score = int(input("请输入需要测评的成绩:\n"))
if 90<=score<=100:
    print("A级")
elif 80<=score<90:
    print("B级")
elif 70<=score<80:
    print("C级")
elif 60<=score<70:
    print("D级")
elif 0<=score<60:
    print("E级")
else:
    print("非法输入")
#输出和变量的应用
print('hello world')
i = 1
print(i)

#文件的创建和输入
fp = open('D:/apython.txt', 'a+')
print('hello world', file=fp)
fp.close()

#解决两个浮点型数字相加结果不准确的方法
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#运算符操作
print(9//4)  #//为整除符号
print(9%-4)  #公式：余数= 被除数-除数*商
print(2**3)  #幂运算

#分支条件
money = 1000
out = int(input("请输入你要取出的金额"))
if money >= out :
    money -= out
    print("取款成功，余额为：",money)
num = int(input("请输入要判断为奇偶的数字"))
if num%2==0:
    print(num,'为偶数')
elif num%7==0:
    print(num,"为7的倍数")

#输入以及对输入的内容进行处理
a = int(input("请输入一个加数:"))
b = int(input("请输入另一个加数:"))
print("a+b = ",a+b)

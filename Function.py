# 开发时间：2023/8/7 23:34
#函数
def fun0(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

def fun1(*args):
    print(args)

def fun2(**args):
    print(args)

def fun3(a,b,*,c):
    print('a=', a)
    print('b=', b)
    print('c=', c)

lst = [1,2,3]
dic = {'a':12,'b':3,'c':10,}
fun0(*lst)  #*lst可以把列表中的数字转化成参数依次付给函数，但个数不能多也不能少
fun0(**dic) #字典内参数必须与函数形参一致
fun1(1,2,3,'abc')
fun2(hou=1,b=2,c=3,e=4)
fun3(1,2,c=3)   #'*'号后面为强制参，智能通过关键字实参输入

def fun4():
    print(hou)

hou = 99
fun4()

#递归函数
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
n = 7
print(n,"的阶乘为",fac(n))
print(str(n)+"的阶乘为"+str(fac(n)))

#斐波那契数列
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(10))
for i in range(1,11):
    print(fib(i))
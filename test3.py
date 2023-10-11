# 开发时间：2023/8/5 11:14
#元组的创建方式
print("--------------元组的创建方式------------------")
t = (10,20,30)
t1 = 'dfj','dkfj'
t2 = ()
t3 = tuple(('hou','fa','zhi'))
for item in t3:
    print(item)
print(t)
print(t1)
print((t2))
print(t3)

#字典生成式
print("--------------字典生成式------------------")
items = {'fruits','foods','others'}
values = {30,50,100}
d = {item.upper():value for item,value in zip(items,values)}
print(d)

#集合的创建
print("--------------集合的创建------------------")
s = {10,20,30,10,40,50}
s1 = set(range(0,500,7))
d = {'hou':20,'fa':20,'hou':30,'hou':20}
print(s)
print(s1)
print(d)

#集合的删除和增加操作
print("--------------集合的删除和增加操作------------------")
s2 = {12,20,30,40,50}
print(s2)
s2.add(60)
s2.update(('abc',11,22))
s2.update([12,22,32,42])
s2.update(({10,90}))
print(s2)
s2.remove(10)       #删除没有的元素会报错
s2.discard('abc')   #删除没有的元素不会报错
s2.pop()
print(s2)
s2.clear()
print(s2)
#集合生成式
s0 = {i*i for i in range(10)}
print(s0)

#字符串操作
r = 'hello,hello'
print(r.index('lo'))
print(r.rindex('lo'))
print(r.find('lo'))
print(r.rfind('lo'))
s = 'hello,python'
print(s.upper())    #全部转大写
print(s.lower())    #全部转小写
print(s.title())    #每个字母首字母大写其他字母小写
print(s.capitalize())   #首字母大写其他字母小写
print(s.swapcase()) #所有大小写字母反转
print(s.center(20,'*')) #中对其
print(s.ljust(20,'*'))
print(s.rjust(20,"*"))
print(s.split(','))
#字符串的替换和拼接
s = "hello,python,python,python"
print(s.replace("python",'java',2))
lst = ['hello','java','python']
print('、'.join(lst))

#字符串格式化
print("我是%s,今年%d岁" % ("hou",20))
print("我是{0}，今年{1}岁".format("hou",20))
print(f"我是{'hou'},今年{20}岁")
print('输出的数字为%10.5d' % 9999) #格式为占十位，保留四位小数
print('输出的数字为{:10.4f}'.format(3.1415926))

#字符串的编码与解码
s = "同是天涯沦落人"
byte = s.encode(encoding='UTF-8')
print(byte)
print(byte.decode(encoding='UTF-8'))
# 开发时间：2023/8/14 15:39
# 开发时间：2023/8/14 15:27
#文件读写操作
file = open('a.txt','a')
file.write('hello world')
file.close()
file = open('a.txt','r')
print(file.readlines())
file.close()
#二进制文件的复制操作
file1 = open('截图.png','rb')
file2 = open('copy.png','ab')
file2.write(file1.read())
file2.close()
file1.close()
#使用with语句上下文管理器实现二进制文件的复制
with open("截图.png",'rb') as file3:
    with open('copy1.png','wb') as file4:
        file4.write(file3.read())

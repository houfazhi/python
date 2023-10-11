# 开发时间：2023/8/14 16:42
#实例一:寻找当前目录下所有相同类型的文件
import os
# print(os.getcwd())
# lst = os.listdir(os.getcwd())
# for filename in lst:
#     if filename.endswith('.png'):
#         print(filename)

#实例二：查看当前文件夹下所有的文件和将所有文件以路径的形式输出
lst_name = os.walk(os.getcwd())
print(lst_name)
for dirpath,dirname,filename in lst_name:
    print(dirpath)
    print('---------------------------')
    print(dirname)
    print('---------------------------')
    print(filename)
    print('---------------------------')
    for dir in dirname:
        print(os.path.join(dirpath, dir))
        print('---------------------------')
    for file in filename:
        print(os.path.join(dirpath,file))

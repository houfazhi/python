# 开发时间：2023/8/14 16:20
#os.path的操作
import os
print(os.getcwd())
print(os.path.abspath('demo2.py'))
print(os.path.exists('demo1.py'))
print(os.path.exists('../tts/demo4.py'))
print(os.path.join('D:\\houfazhi','wegame'))
print(os.path.splitext(os.getcwd()))
print('---------------------------------')
print(os.path.split(os.getcwd()))
print(os.path.basename(os.getcwd()))
print(os.path.dirname(os.getcwd()))
print(os.path.isdir(os.getcwd()))
print(os.path.isdir('D:\C-primer\python\file\demo2.py'))
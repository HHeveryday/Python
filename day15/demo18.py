# 列出指定目录下的所有python文件
import os
path = os.getcwd()
print(path)
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)

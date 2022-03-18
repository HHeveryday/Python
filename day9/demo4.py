'''字符串的对其方式'''
s = 'hello,python'
print(s.center(20, '*'))  # 居中

print(s.ljust(20, '*'))  # 左对齐

print(s.rjust(20, '*'))  # 右对齐

print(s.zfill(20))  # 右对齐，使用0填充

print('-231'.zfill(8))

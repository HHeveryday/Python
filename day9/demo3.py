'''字符串的大小写转换'''
s = 'HeLlo,world'
print(s)
a = s.upper()  # 转换为大写后会产生一个新的字符串对象
print(a)
b = s.lower()  # 转换为小写
print(b)
print(s.swapcase())  # 大写转小写，小写转大写

print(s.capitalize())  # 第一个字符串大写，后面的小写

print(s.title())  # 首字母大写

# 字符串的驻留机制
a = 'hello'
b = "hello"
c = '''hello'''
print(a, id(a))
print(b, id(b))
print(c, id(c))

s1 = 'abc%'
s2 = 'abc%'
print(a is b)

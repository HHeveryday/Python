# 元组的创建方式
'''直接使用小括号()'''
from this import d


t = ('hello', 'world', 23)
print(t, type(t))
t1 = 'hello', 'world', 65
print(t1, type(t1))

'''第二种方式，使用内置函数tuple()'''
t2 = tuple(('hello', 'world', 65))
print(t2, type(t2))

'''元组只有一个元素时需要加逗号'''
t3 = ('hello')
print(type(t3))
t4 = ('hello',)
print(type(t4))


'''空列表、空字典的创建方式'''
l = []
l1 = list()

d = {}
d1 = dict()

'''空元组的创建方式'''
t5 = ()
t6 = tuple()

print('空列表和空字典：', l, l1, d, d1)
print('空元组：', t5, t6)

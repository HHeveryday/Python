'''集合的相关操作'''
from re import S


s = {10, 10, 45, 62}
print(10 in s)


'''集合元素的添加操作'''
s.add(80)  # 只添加一个元素
print(s)
s.update({200, 300})  # 至少添加一个元素
print(s)
s.update((20, 12, 36))
print(s)
'''集合元素的删除操作'''

s.remove(200)  # 没有会报错
print(s)

s.discard(500)  # 没有不会报错
print(s)

s.pop()
print(s)

s.clear()
print(s)

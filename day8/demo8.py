'''集合的数学操作'''
# 交集
s1 = {10, 20, 30}
s2 = {20, 30, 40, 50}
print(s1.intersection(s2))
print(s1 & s2)  # intersection()方法与 & 等价，都是求交集

# 求并集
print(s1.union(s2))
print(s1 | s2)  # union()方法与 | 等价，都是求并集

# 差集操作
print(s1.difference(s2))
print(s1-s2)  # difference()方法与 - 等价，都是求并集

# 对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

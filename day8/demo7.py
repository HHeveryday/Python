s = {10, 20, 65}
s1 = {30, 54, 58}
print(s == s1)

'''一个集合是否为另一个集合的子集'''

s2 = {10, 20, 30, 40}
s3 = {10, 20, 30, 40, 50}
s4 = {10, 20, 62, 52}
print(s2.issubset(s3))
print(s2.issubset(s4))

'''一个集合是否为另一个集合的超集'''

print(s3.issuperset(s2))

'''判断交集'''
s5 = {99, 66}
print(s2.isdisjoint(s5))  # True  没有交集为True

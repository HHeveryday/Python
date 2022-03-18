'''可变序列与不可变序列'''

'''可变序列 列表，字典'''
lst = [10, 20, 30]
print(lst, id(lst))
lst.append(200)

print(lst, id(lst))

'''不可变序列  字符串，元组'''
s = 'hello'
print(id(s))
s = s+'world'
print(s, id(s))

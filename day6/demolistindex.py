lst=['hello','world',98,'hello']
print(lst.index('hello'))#如果列表中有相同元素，只返回列表中第一个元素的索引
# print(lst.index('hh'))#不在列表中会返回异常

print(lst.index('hello',1,4))
from optparse import Values


scores={'张三':100,'李四':20,'王五':50}
#获取所有的key
keys=scores.keys()
print(keys,type(keys))

print(list(keys)) #将所得的键转换为列表

values=scores.values()
print(values,type(values))

print(list(values))
item=scores.items()
print(item,type(item))
print(list(item))#转换之后的列表元素是由元组组成的
#字典中元素的获取
scores={'张三':100,'李四':20,'王五':50}
print(scores['张三'])


print(scores.get('张三'))

print(scores.get('马七'))
print(scores.get('马七',23))#23为查找不存在时提供的默认值
print(scores.get('李四',23))#23为查找不存在时提供的默认值
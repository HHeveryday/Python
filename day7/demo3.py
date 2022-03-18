from sys import orig_argv


scores={'张三':100,'李四':20,'王五':50}

'''key的判断'''
print('张三' in scores)
print('张三' not in scores)

'''del删除字典中的键值对'''

del scores['张三']
print(scores)
# scores.clear()#清空字典

scores['陈六']=100#新增
print(scores)
scores['陈六']=98#修改
print(scores)
t = (20, [10, 20], 60)
print(t, type(t))
print(t[0], type(t[0]), id(t[0]))
print(t[1], type(t[1]), id(t[1]))
print(t[2], type(t[2]), id(t[2]))
'''尝试将t[1]修改为100'''
print(id(100))
# t[1] = 100#元组不允许修改元素
t[1].append(100)  # 列表是可变序列，所以可以向列表中添加元素，而列表的内存地址不会改变
print(t)

# name = '张三'
# age = 20

# print(type(name),type(age))
# # print('我叫'+name+'今年,'+age+'岁')#当将str类型与int类型进行连接时，报错，解决方案，类型转换
# print('我叫'+name+'今年,'+str(age)+'岁')#当将str类型与int类型进行连接时，报错，解决方案，类型转换

# print('-----str()将其他类型转换为str类型')
# a = 10
# b = 10.2
# c = False
# print(type(a),type(b),type(c))
# print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

# print('----------int()将其他的类型装换为int类型')
# s1 = '128'
# f1 = 52.2
# s2 = '52.2'
# ff = True
# s3 = 'hello world'
# print(type(s1),type(f1),type(s2),type(ff),type(s3))
# print(int(s1),type(int(s1)))#将str类型转换为int类型，字符串为数字串
# print(int(f1),type(int(f1)))#将float转换为int类型，截取整数部分，舍掉小数部分
# # print(int(s2),type(int(s2)))#将str转换成int类型，报错，因为字符串为小数串
# print(int(ff),type(int(ff)))
# print(int(s3),type(s3))#报错，将str转换为int类型时，字符串必须为数字串（整数），非数字串是不允许转换的



print('---------float()函数，将其他类型转换为float类型')
s1 = '52.2'
s2 = '52'
ff = True
s3 = 'hello'
i = 98
print(type(s1),type(s2),type(ff),type(s3),type(i))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
# print(float(s3),type(float(s3)))#字符串中的数据不是数字串，则不允许转换

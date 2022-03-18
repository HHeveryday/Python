'''格式化字符串的方式'''
#NOTE(1) % 占位符
name = "张三"
age = 20
print('我叫%s,今年%d岁' % (name, age))


# NOTE(2)使用{}
print('我叫{0},今年{1}岁了'.format(name, age))


# NOTE(3) f-string
print(f'我叫{name},今年{age}岁了')

'''异常处理机制'''
try:
    a = int(input('请输入一个整数：'))
    b = int(input('请输入另一个整数：'))
    result = a/b
    print('结果为：', result)
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('只能为数字串')

print('程序结束')

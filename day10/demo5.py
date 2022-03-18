def fun(*args):  # 函数定义时的可变位置参数
    print(args)


fun(10)
fun(10, 20, 30)
fun(10, 20, 30, 40)


def fun1(**agrs):
    print(agrs)


fun1(a=10)
fun1(a=20, b=30, c=40)


'''
可变位置和可变关键字参数都只能定义一个
'''


def fun2(*agrs1, **agrs2):
    pass
# def fun3(**agrs1,*agrs2):
#     pass


'''在一个函数的定义过程中，既有个数关键字参数形参又有个数可变的位置型形参，要求个数可变的位置型形参要放在前面'''

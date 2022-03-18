def fun(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


print(fun([10, 21, 30, 32, 23, 48]))

'''
(1)函数的返回值没有，可以不用写retrun
(2)函数的返回值如果是一个，直接返回原值
(3)函数的返回值如果有多个，则返回的值为元组


'''

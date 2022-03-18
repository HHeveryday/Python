def fun(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


fun(10, 20, 30)
lst = [10, 20, 30]
fun(*lst)
fun(a=100, b=200, c=300)
dic = {'a': 101, 'b': 201, 'c': 301}
fun(**dic)

#NOTE赋值运算符，运算顺序从右到左

i = 3+4
print(i)
a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))


print('------参数赋值-------')
a = 20
a+=20
print(a)


print('-----解包赋值-----')
a,b,c=20,30,40
print(a,b,c)

print('-------交换两个变量的值')
a,b=20,30
print('交换之前：',a,b)
a,b=b,a
print('交换之后的值：',a,b)
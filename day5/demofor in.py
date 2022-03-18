for i in 'hello world':#第一次取出来的值为h，在依次把hello world赋值给i进行输出
    print(i)

for x in range(5):
    print(x)

#如果在循环体中不需要使用到自定义变量，可将自定义变量写为'_'
for _ in range(5):
    print('你好')

print('使用for循环计算1到100之间的偶数和')
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
print(sum)
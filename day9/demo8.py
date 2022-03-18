'''字符串的替换'''
s = 'hello,python'
print(s.replace('python', 'java'))
s1 = 'hello,python,python,python'
print(s1.replace('python', 'java', 2))

lst = ['hello', 'python', 'java']
print('|'.join(lst))
print(''.join(lst))

t = ('hello', 'python', 'java')
print(''.join(t))

'''字符串的分割'''
s = 'hello world python'
lst = s.split()
print(lst)

s1 = 'hello|world|python'
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))

'''rsplit()从右侧开始分'''
print(s.rsplit())

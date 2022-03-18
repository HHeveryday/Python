lst=[12,23,52,266,58,2,9,45]
'''start=1,stop=6,step=1'''
# print(lst[1:6:1])
print('原列表',id(lst))
lst2=lst[1:6:1]
print('切的片段',id(lst2))
print(lst[1:6])#默认步长为1
print(lst[1:6:])
print(lst[1::2])

print('步长为负数的情况')
print(lst[::-1])
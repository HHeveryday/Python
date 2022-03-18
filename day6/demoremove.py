#NOTE删除操作
lst=[10,20,30,6,60,56,3,5,98]
print(lst)
lst.remove(30)#从列表中移除一个元素，有重复只移除第一个元素
print(lst)

#NOTE根据索引移除元素
lst.pop(1)
print(lst)
lst.pop()#如果不指定索引，将删除列表中的最后一个元素
print(lst)


print('-------切片操作---------')
new_lst=lst[1:3]
print(lst)
print(new_lst)

'''不产生新的列表对象，而是删除原列表中的内容'''
lst[1:3]=[]
print(lst)

'''清除列表中的所有元素'''
lst.clear()
print(lst)


'''删除列表'''
del lst
# print(lst)  NameError: name 'lst' is not defined. Did you mean: 'list'?
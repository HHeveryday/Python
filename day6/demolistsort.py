lst=[20,36,5,32,18]
print('排序前的列表',lst,id(lst))
#开始排序，调用列表对象的sort方法，升序排序
lst.sort()
print('排序后的列表',lst,id(lst))

#指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True) #reverse=True表示降序，reverse=False为升序
print(lst)
lst.sort(reverse=False) #reverse=True表示降序，reverse=False为升序
print(lst)


print('---------------------使用内置函数sorted()对列表进行排序，将产生一个新的列表----------------------------------')
lst=[20,36,5,32,18]
print('排序前的列表',lst,id(lst))
new_lst=sorted(lst)
print(lst)
print(new_lst)
#指定关键字参数，实现列表元素的降序排序
dsc_lst=sorted(lst,reverse=True)
print(dsc_lst)
#NOTE向列表的末尾添加一个元素
lst=[10,20,30]
print('添加之前',lst)
print(id(lst))
lst.append(100)
print('添加元素之后',lst)
print(id(lst))
lst2=[10,20,30,42]
lst.append(lst2)
print(lst)
lst.extend(lst2)
print(lst)
#NOTE在任意位置添加元素
lst.insert(1,92)
print(lst)

#在任意位置上添加N多个元素
lst3=[12,'ds','a',98]
lst[1:]=lst3
print(lst)

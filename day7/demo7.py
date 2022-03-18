
# 字典生成式
items = ['Fruits', 'Books', 'Others']
prices = [98, 65, 56]

dict = {item.upper(): price for item, price in zip(items, prices)}
print(dict)

# 字典元素的遍历
scores = {'张三': 100, '李四': 20, '王五': 50}

for item in scores:
    print(item, scores[item], scores.get(item))

#使用条件比较两个整数的大小

num_a=int(input('请输入一个整数：'))
num_b=int(input('请输入另外一个整数：'))
print(str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b))
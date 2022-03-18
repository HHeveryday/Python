# 转义字符
print('hello\nworld')#n表示换行
print('hello\tworld')#t表示制表位
print('hello\rworld')#t表示回车 world将hello覆盖
print('hello\bworld')#b表示退一个格，o没有了
print('http:\\\\baidu.com')#两个\\输出一个\
print('老师说\'你好\'')#\'表示输出'



# 原字符，不希望字符串中的转义字符起作用，就使用原字符，在字符串前加R或者r
print(r'hello\rworld')
#注意，最后一个字符不能为反斜杠
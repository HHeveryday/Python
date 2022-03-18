'''编码'''
s = '天涯共此时'
byte = s.encode(encoding='GBK')
print(s.encode(encoding='GBK'))  # 一个中文占两个字节
print(s.encode(encoding='UTF-8'))  # 一个中文占三个字节

'''解码'''
print(byte.decode(encoding='GBK'))

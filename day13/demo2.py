# 在demo8中导入pageage
import imp
import sys
import pageage.module_A as a
import time
import urllib.request
print(a.a)
print(sys.getsizeof(10))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())
print(time.localtime(time.time()))
print(urllib.request.urlopen('http://www.baidu.com').read())

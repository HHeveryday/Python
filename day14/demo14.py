import os
os.chdir('C:\\Users\\16043\\Desktop\\CODE\\PYTHON\\day14')#将path设置为当前工作目录
with open('1.jpg', 'rb') as src_file:
    with open('copy5.jpg', 'wb') as target_file:
        target_file.write(src_file.read())

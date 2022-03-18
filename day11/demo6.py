class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name+'在吃饭')


stu1 = Student('张三', 20)
stu2 = Student('李四', 21)
print('============为stu2绑定性别属性==================')
stu2.gender = '女'
print(stu1.name, stu1.age)
print(stu2.name, stu2.age, stu2.gender)


def show():
    print('定义在类之外，称函数')


stu1.show = show
stu1.show()


# stu2.show() stu2会报错，因为并没有绑定show方法
